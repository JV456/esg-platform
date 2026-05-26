from django.db import models
from organizations.models import Organization
from ingestion.models import RawRecord


class EmissionRecord(models.Model):

    REVIEW_STATUS = [
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    ]

    SCOPE_CHOICES = [
        ("SCOPE_1", "SCOPE_1"),
        ("SCOPE_2", "SCOPE_2"),
        ("SCOPE_3", "SCOPE_3"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="emission_records"
    )

    raw_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE,
        related_name="emission_records"
    )

    activity_type = models.CharField(
        max_length=255
    )

    scope = models.CharField(
        max_length=50,
        choices=SCOPE_CHOICES
    )

    quantity = models.FloatField()

    unit = models.CharField(
        max_length=50
    )

    normalized_unit = models.CharField(
        max_length=50
    )

    co2e_emission = models.FloatField()

    start_date = models.DateField(
        null=True,
        blank=True
    )

    end_date = models.DateField(
        null=True,
        blank=True
    )

    source_reference = models.CharField(
        max_length=255,
        blank=True
    )

    review_status = models.CharField(
        max_length=50,
        choices=REVIEW_STATUS,
        default="PENDING"
    )

    is_flagged = models.BooleanField(
        default=False
    )

    locked_for_audit = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.activity_type} - {self.scope}"