from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, ShopItemViewSet, index, get_user
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'shop_items', ShopItemViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('auth/user/', get_user, name='get_user'),  # Custom user endpoint
    path('auth/token/', obtain_auth_token, name='api_token_auth'),  # Optional token login

]