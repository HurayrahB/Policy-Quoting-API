from django.core.cache import cache

from django.shortcuts import render
from decimal import Decimal
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Applicant, Quote
from .serializers import ApplicantSerializer, QuoteSerializer

PROVINCE_FACTOR = {
    "ON": Decimal("1.10"),
    "AB": Decimal("0.95"),
    "BC": Decimal("1.05"),
    "QC": Decimal("1.00"),
    "NS": Decimal("0.98"),
}
BASE_RATE = Decimal("0.0012")

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        return Quote.objects.select_related("applicant").order_by("id")

    @action(detail=True, methods=["post"])
    def price(self, request, pk=None):
        quote = self.get_object()
        key = f"premium:{quote.pk}:{quote.coverage_amount}"

        cached = cache.get(key)
        if cached is not None:
            premium = Decimal(cached)
        else:
            factor = PROVINCE_FACTOR.get(quote.applicant.province, Decimal("1.00"))
            premium = (quote.coverage_amount * BASE_RATE * factor).quantize(Decimal("0.01"))
            cache.set(key, str(premium), timeout=300)

        quote.premium = premium
        quote.save(update_fields=["premium"])
        return Response(
            {"id": quote.pk, "premium": premium, "cache_hit": cached is not None}
        )
