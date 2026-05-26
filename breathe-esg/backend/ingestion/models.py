from django.db import models
from organizations.models import Organization


class DataSource(models.Model):

    SOURCE_TYPES = [
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL"),
    ]

    INGESTION_METHODS = [
        ("CSV", "CSV"),
        ("API", "API"),
        ("PDF", "PDF"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="data_sources"
    )

    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPES
    )

    ingestion_method = models.CharField(
        max_length=50,
        choices=INGESTION_METHODS
    )

    uploaded_file_name = models.CharField(
        max_length=255,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.organization.name} - {self.source_type}"
    
    
class RawRecord(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("PROCESSED", "PROCESSED"),
        ("FAILED", "FAILED"),
    ]

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE,
        related_name="raw_records"
    )

    raw_payload = models.JSONField()

    ingestion_status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    error_message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"RawRecord {self.id}"