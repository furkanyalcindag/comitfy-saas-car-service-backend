from django.db import models

from carService.models.Organization import Organization


class Supplier(models.Model):
    firmName = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    firstName = models.CharField(max_length=255, null=True, blank=True)
    lastName = models.CharField(max_length=255, null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
