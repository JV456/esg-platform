from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from emissions.models import EmissionRecord
from audit.models import AuditLog

from .serializers import ReviewRecordSerializer
from .dashboard_serializers import DashboardMetricsSerializer


class DashboardMetricsView(APIView):

    def get(self, request):

        total_records = EmissionRecord.objects.count()

        pending_reviews = EmissionRecord.objects.filter(
            review_status="PENDING"
        ).count()

        approved_records = EmissionRecord.objects.filter(
            review_status="APPROVED"
        ).count()

        rejected_records = EmissionRecord.objects.filter(
            review_status="REJECTED"
        ).count()

        flagged_records = EmissionRecord.objects.filter(
            is_flagged=True
        ).count()

        data = {
            "total_records": total_records,
            "pending_reviews": pending_reviews,
            "approved_records": approved_records,
            "rejected_records": rejected_records,
            "flagged_records": flagged_records,
        }

        serializer = DashboardMetricsSerializer(data)

        return Response(serializer.data)


class PendingReviewListView(APIView):

    def get(self, request):

        records = EmissionRecord.objects.filter(
            review_status="PENDING"
        ).order_by("-created_at")

        serializer = ReviewRecordSerializer(
            records,
            many=True
        )

        return Response(serializer.data)


class FlaggedRecordsView(APIView):

    def get(self, request):

        records = EmissionRecord.objects.filter(
            is_flagged=True
        )

        serializer = ReviewRecordSerializer(
            records,
            many=True
        )

        return Response(serializer.data)


class ApproveRecordView(APIView):

    def post(self, request, record_id):

        try:

            record = EmissionRecord.objects.get(id=record_id)

            if record.locked_for_audit:
                return Response(
                    {"error": "Record already locked"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            old_status = record.review_status

            record.review_status = "APPROVED"

            record.locked_for_audit = True

            record.save()

            AuditLog.objects.create(
                emission_record=record,
                changed_by=request.user if request.user.is_authenticated else None,
                field_name="review_status",
                old_value=old_status,
                new_value="APPROVED"
            )

            return Response({
                "message": "Record approved successfully"
            })

        except EmissionRecord.DoesNotExist:

            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class RejectRecordView(APIView):

    def post(self, request, record_id):

        try:

            record = EmissionRecord.objects.get(id=record_id)

            if record.locked_for_audit:
                return Response(
                    {"error": "Record already locked"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            old_status = record.review_status

            record.review_status = "REJECTED"

            record.save()

            AuditLog.objects.create(
                emission_record=record,
                changed_by=request.user if request.user.is_authenticated else None,
                field_name="review_status",
                old_value=old_status,
                new_value="REJECTED"
            )

            return Response({
                "message": "Record rejected successfully"
            })

        except EmissionRecord.DoesNotExist:

            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )