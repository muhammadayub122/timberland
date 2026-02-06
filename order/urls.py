from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (OrderApiiview, OrderProductApiiview, AddressApiiview)

router = DefaultRouter()
router.register(r"order", OrderApiiview)
router.register(r"orderproduct", OrderProductApiiview)
router.register(r"address", AddressApiiview)

urlpatterns = [
    path("", include(router.urls)),
]
