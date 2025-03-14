from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("stock_manager.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("stock_manager.urls")),  # Your app API
    path("accounts/", include("django.contrib.auth.urls")),  # Django login/logout
    path("api/auth/", include("rest_framework.urls")),  # ✅ Add DRF auth endpoints
]
