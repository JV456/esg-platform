from rest_framework import serializers
from emissions.models import EmissionRecord


class ReviewRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmissionRecord
        fields = "__all__"