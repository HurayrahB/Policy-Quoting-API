from decimal import Decimal

import pytest
from rest_framework.test import APIClient

from quotes.models import Applicant, Quote


@pytest.fixture
def fifty_quotes(db):
    for i in range(50):
        applicant = Applicant.objects.create(
            name=f"Applicant {i}", province="ON", date_of_birth="1990-01-01"
        )
        Quote.objects.create(applicant=applicant, coverage_amount=Decimal("100000.00"))


def test_quote_list_query_count(fifty_quotes, django_assert_num_queries):
    client = APIClient()
    with django_assert_num_queries(1):
        response = client.get("/api/quotes/")
    assert response.status_code == 200
    assert len(response.json()) == 50