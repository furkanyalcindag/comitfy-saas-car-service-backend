from django.db import models

from carService.models.BaseModel import BaseModel


class Organization(BaseModel):
    name = models.CharField(max_length=256)
    taxNumber = models.CharField(max_length=128)
    taxOffice = models.CharField(max_length=128)
    mobilePhone = models.CharField(max_length=128)
    logo = models.TextField()
    isActive = models.BooleanField()
    email = models.EmailField()
    subdomain = models.CharField(max_length=256, unique=True)
