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
            item=self,
            shop_user=shop_user,
            defaults={
                'xfer_pending': self.xfer_pending,
                'last_updated': self.last_updated,
            }
        )

        shop_item.quantity += transfer_quantity
        shop_item.save()


class ShopItem(models.Model):
    id = models.AutoField(primary_key=True)  # Add primary key field
    shop_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relates item to a User
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=1)  # Relates ShopItem to Item with a default value
    quantity = models.IntegerField(default=0)
    xfer_pending = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shop_user.username} - {self.item.sku}"
