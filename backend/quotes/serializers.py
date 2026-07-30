from rest_framework import serializers
from .models import Applicant, Quote

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ["id", "name", "province", "date_of_birth"]

class QuoteSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)
    applicant_id = serializers.PrimaryKeyRelatedField(
        queryset=Applicant.objects.all(), source="applicant", write_only=True
    )

    class Meta:
        model = Quote
        fields = [
            "id",
            "applicant",
            "applicant_id",
            "coverage_amount",
            "premium",
            "status",
            "created_at",
        ]
        read_only_fields = ["premium", "created_at"]

    def validate_coverage(self, value):
        if value <= 0:
            raise serializers.ValidationError("Coverage amount must be positive.")
        return value

