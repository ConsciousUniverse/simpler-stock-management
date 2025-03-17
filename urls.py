from django.urls import path
from . import views

urlpatterns = [
    path('api/get_edit_lock_status/', views.get_edit_lock_status, name='get_edit_lock_status'),
]