from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    sku = models.CharField(primary_key=True, unique=True, editable=True, max_length=100)
    description = models.CharField(max_length=250)
    retail_price = models.FloatField()
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku


class ShopItem(models.Model):
    shop_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relates item to a User
    sku = models.CharField(primary_key=True, unique=True, editable=True, max_length=100)
    description = models.CharField(max_length=250)
    retail_price = models.FloatField()
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku
