from django.db import models

from carService.models.BaseModel import BaseModel
from carService.models.Organization import Organization
from carService.models.Plan import Plan


class Subscription(BaseModel):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    isMonthly = models.BooleanField()
    isYearly = models.BooleanField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    isActive = models.BooleanField()
    startDate = models.DateField()
    expiryDate = models.DateField()
