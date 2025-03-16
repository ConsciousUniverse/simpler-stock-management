from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Item, ShopItem
from .serializers import ItemSerializer, ShopItemSerializer
from .pagination import CustomPagination
from django.contrib.auth.models import User  # For accessing the User model
from rest_framework.response import (
    Response,
)  # For returning HTTP responses in REST framework
from rest_framework.decorators import api_view


# API View
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "sku"
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination 

    def get_queryset(self):
        queryset = Item.objects.all()
        search_query = self.request.query_params.get("search", None)
        if search_query:
            queryset = queryset.filter(
                description__icontains=search_query
            )  # 🔍 Search filter
        queryset = queryset.order_by('sku')
        return queryset


class ShopItemViewSet(viewsets.ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
    lookup_field = "sku"
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination 

    def get_queryset(self):
        queryset = ShopItem.objects.filter(shop_user=self.request.user)
        search_query = self.request.query_params.get("search", None)
        if search_query:
            queryset = queryset.filter(
                description__icontains=search_query
            )  # 🔍 Search filter
        queryset = queryset.order_by('sku')
        return queryset


# Main Page View
@login_required
def index(request):
    return render(request, "index.html")


@api_view(["GET"])
def get_user(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return Response(
            {"detail": "Authentication credentials were not provided."}, status=401
        )

    user = request.user
    return Response(
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "groups": list(user.groups.values_list("name", flat=True)),
        }
    )
