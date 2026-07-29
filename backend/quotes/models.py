from django.db import models

class Applicant(models.Model):
    name = models.CharField(max_length=120)
    province = models.CharField(max_length=2)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Quote(models.Model):
    STATUS_CHOICES = [
        ("draft","Draft"),
        ("bound","Bound"),
        ("expired","Expired"),
    ]

    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name="quotes"
    )

    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)
    premium = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote {self.pk} for {self.applicant_id}"