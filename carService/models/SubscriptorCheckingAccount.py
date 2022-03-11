from django.db import models

from carService.models.BaseModel import BaseModel
from carService.models.Subscription import Subscription


class SubscriptionCheckingAccount(BaseModel):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
    remainingDebt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    isPaid = models.BooleanField(default=False)
