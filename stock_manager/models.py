from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    sku = models.CharField(primary_key=True, unique=True, editable=True, max_length=100)
    description = models.CharField(max_length=250)
    retail_price = models.FloatField()
    quantity = models.IntegerField()
    xfer_pending = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku

    def transfer_to_shop(self, shop_user, transfer_quantity):
        if self.quantity < transfer_quantity:
            raise ValueError("Not enough stock to transfer")

        self.quantity -= transfer_quantity
        self.save()

        shop_item, created = ShopItem.objects.get_or_create(
            sku=self.sku,
            shop_user=shop_user,
            defaults={
                'description': self.description,
                'retail_price': self.retail_price,
                'quantity': 0,  # Initialize with 0, will be updated below
            }
        )

        shop_item.quantity += transfer_quantity
        shop_item.save()


class ShopItem(models.Model):
    shop_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relates item to a User
    sku = models.CharField(primary_key=True, unique=True, editable=True, max_length=100)
    description = models.CharField(max_length=250)
    retail_price = models.FloatField()
    quantity = models.IntegerField()
    xfer_pending = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku
