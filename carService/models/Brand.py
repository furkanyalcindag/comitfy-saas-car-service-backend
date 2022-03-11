from django.db import models

from carService.models.Organization import Organization


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)