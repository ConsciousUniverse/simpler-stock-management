from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, ShopItemViewSet, index, get_user, transfer_item, toggle_update_mode, get_edit_lock_status  # Add get_edit_lock_status import
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'shop_items', ShopItemViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('auth/user/', get_user, name='get_user'),  # Custom user endpoint
    path('auth/token/', obtain_auth_token, name='api_token_auth'),  # Optional token login
    path('api/transfer/', transfer_item, name='transfer_item'),  # Add this line
    path('api/toggle_update_mode/', toggle_update_mode, name='toggle_update_mode'),  # Ensure correct import
    path('api/get_edit_lock_status/', get_edit_lock_status, name='get_edit_lock_status'),  # Add this line
]