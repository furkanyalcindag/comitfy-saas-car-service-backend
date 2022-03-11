from django.db import models

from carService.models.BaseModel import BaseModel


class AppStore(BaseModel):
    name = models.CharField(max_length=256)
