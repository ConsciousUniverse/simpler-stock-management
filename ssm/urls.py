from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("stock_manager.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("stock_manager.urls")),  # Your app API
    path("accounts/", include("django.contrib.auth.urls")),  # Django login
    path("api/auth/", include("rest_framework.urls")),  # ✅ Add DRF auth endpoints
]