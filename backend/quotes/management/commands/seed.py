import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from quotes.models import Applicant, Quote

PROVINCES = ["ON", "AB", "BC", "AB", "NS"]

class Command(BaseCommand):
    help = "Wipe and reseed applicants and quotes."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=50)

    def handle(self, *args, **options):
        count = options["count"]
        Quote.objects.all().delete()
        Applicant.objects.all().delete()

        for i in range(count):
            applicant = Applicant.objects.create(
                name=f"Applicant {i:03d}",
                province=random.choice(PROVINCES),
                date_of_birth="1990-01-01"
            )
            Quote.objects.create(
                applicant=applicant,
                coverage_amount=Decimal(random.randrange(50_000,1_000_000,10_000)),
            )

        self.stdout.write(self.style.SUCCESS(f"Seeded {count} applicants and quotes."))