from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from igaveapp.views import UserViewSet, ReceiptViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"receipts", ReceiptViewSet, basename="receipt")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
