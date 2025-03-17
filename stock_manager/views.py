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
from django.db.models.functions import Lower
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError


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
        ordering = self.request.query_params.get("ordering", None)
        if ordering:
            if ordering.startswith('-'):
                queryset = queryset.order_by(Lower(ordering[1:])).reverse()
            else:
                queryset = queryset.order_by(Lower(ordering))
        else:
            queryset = queryset.order_by(Lower('sku'))
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
        ordering = self.request.query_params.get("ordering", None)
        if ordering:
            if ordering.startswith('-'):
                queryset = queryset.order_by(Lower(ordering[1:])).reverse()
            else:
                queryset = queryset.order_by(Lower(ordering))
        else:
            queryset = queryset.order_by(Lower('sku'))
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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def transfer_item(request):
    if not request.user.groups.filter(name='shop_users').exists():
        return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

    sku = request.data.get("sku")
    transfer_quantity = int(request.data.get("transfer_quantity", 0))

    if transfer_quantity <= 0:
        return Response({"detail": "Transfer quantity must be greater than zero."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        item = Item.objects.get(sku=sku)
        item.transfer_to_shop(request.user, transfer_quantity)
    except Item.DoesNotExist:
        return Response({"detail": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail": "Transfer successful."}, status=status.HTTP_200_OK)
