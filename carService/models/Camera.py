from django.db import models

from carService.models.Organization import Organization


class Camera(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255,blank=True, null=True)