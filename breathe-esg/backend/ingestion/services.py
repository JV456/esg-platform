import pandas as pd
import json

from organizations.models import Organization
from ingestion.models import DataSource, RawRecord
from emissions.models import EmissionRecord


def process_sap_csv(file_path, organization_id):

    organization = Organization.objects.get(id=organization_id)

    data_source = DataSource.objects.create(
        organization=organization,
        source_type="SAP",
        ingestion_method="CSV",
        uploaded_file_name=file_path.name
    )

    df = pd.read_csv(file_path)

    for _, row in df.iterrows():

        raw_record = RawRecord.objects.create(
            data_source=data_source,
            raw_payload=row.to_dict(),
            ingestion_status="PROCESSED"
        )

        quantity = float(row["Menge"])

        is_flagged = quantity > 100000

        EmissionRecord.objects.create(
            organization=organization,
            raw_record=raw_record,

            activity_type=row["Kraftstoff"],

            scope="SCOPE_1",

            quantity=quantity,

            unit=row["Einheit"],

            normalized_unit=row["Einheit"],

            co2e_emission=quantity * 2.5,

            source_reference=row["Belegnummer"],

            is_flagged=is_flagged
        )


def process_utility_csv(file_path, organization_id):

    organization = Organization.objects.get(id=organization_id)

    data_source = DataSource.objects.create(
        organization=organization,
        source_type="UTILITY",
        ingestion_method="CSV",
        uploaded_file_name=file_path.name
    )

    df = pd.read_csv(file_path)

    for _, row in df.iterrows():

        raw_record = RawRecord.objects.create(
            data_source=data_source,
            raw_payload=row.to_dict(),
            ingestion_status="PROCESSED"
        )

        kwh = float(row["kwh"])

        is_flagged = kwh <= 0

        EmissionRecord.objects.create(
            organization=organization,
            raw_record=raw_record,

            activity_type="Electricity Usage",

            scope="SCOPE_2",

            quantity=kwh,

            unit="kWh",

            normalized_unit="kWh",

            co2e_emission=kwh * 0.4,

            source_reference=row["meter_id"],

            is_flagged=is_flagged
        )


def process_travel_json(file_path, organization_id):

    organization = Organization.objects.get(id=organization_id)

    data_source = DataSource.objects.create(
        organization=organization,
        source_type="TRAVEL",
        ingestion_method="API",
        uploaded_file_name=file_path.name
    )

    data = json.load(file_path)

    for item in data:

        raw_record = RawRecord.objects.create(
            data_source=data_source,
            raw_payload=item,
            ingestion_status="PROCESSED"
        )

        if item["trip_type"] == "flight":

            distance = item.get("distance_km", 0)

            is_flagged = (
                item["origin"] == item["destination"]
            )

            EmissionRecord.objects.create(
                organization=organization,
                raw_record=raw_record,

                activity_type="Flight Travel",

                scope="SCOPE_3",

                quantity=distance,

                unit="km",

                normalized_unit="km",

                co2e_emission=distance * 0.15,

                source_reference=f'{item["origin"]}-{item["destination"]}',

                is_flagged=is_flagged
            )

        elif item["trip_type"] == "hotel":

            nights = item.get("hotel_nights", 0)

            EmissionRecord.objects.create(
                organization=organization,
                raw_record=raw_record,

                activity_type="Hotel Stay",

                scope="SCOPE_3",

                quantity=nights,

                unit="nights",

                normalized_unit="nights",

                co2e_emission=nights * 12,

                source_reference=item["city"],

                is_flagged=False
            )