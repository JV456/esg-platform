from rest_framework import serializers


class DashboardMetricsSerializer(serializers.Serializer):

    total_records = serializers.IntegerField()

    pending_reviews = serializers.IntegerField()

    approved_records = serializers.IntegerField()

    rejected_records = serializers.IntegerField()

    flagged_records = serializers.IntegerField()