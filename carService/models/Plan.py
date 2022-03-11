from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=128, null=True)
    maxUserCount = models.IntegerField()
    stockTracking = models.BooleanField()
    netPriceMonthly = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    netPriceYearly = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxRate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
