from django.db import models

from carService.models.Organization import Organization


class Category(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
