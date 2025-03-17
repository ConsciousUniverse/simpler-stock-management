from rest_framework import serializers
from .models import Item, ShopItem
from django.contrib.auth.models import User, Group


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["sku", "description", "retail_price", "quantity", "xfer_pending"]


class ShopItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ShopItem
        fields = ["shop_user", "item", "quantity", "xfer_pending", "last_updated"]
