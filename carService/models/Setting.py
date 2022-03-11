from django.db import models

from carService.models.Organization import Organization


class Setting(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField()
