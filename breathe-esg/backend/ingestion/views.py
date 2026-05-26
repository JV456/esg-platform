from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import (
    process_sap_csv,
    process_utility_csv,
    process_travel_json
)


class SAPUploadView(APIView):

    def post(self, request):

        file = request.FILES.get("file")

        organization_id = request.data.get("organization_id")

        process_sap_csv(file, organization_id)

        return Response(
            {"message": "SAP data uploaded successfully"},
            status=status.HTTP_201_CREATED
        )


class UtilityUploadView(APIView):

    def post(self, request):

        file = request.FILES.get("file")

        organization_id = request.data.get("organization_id")

        process_utility_csv(file, organization_id)

        return Response(
            {"message": "Utility data uploaded successfully"},
            status=status.HTTP_201_CREATED
        )


class TravelUploadView(APIView):

    def post(self, request):

        file = request.FILES.get("file")

        organization_id = request.data.get("organization_id")

        process_travel_json(file, organization_id)

        return Response(
            {"message": "Travel data uploaded successfully"},
            status=status.HTTP_201_CREATED
        )