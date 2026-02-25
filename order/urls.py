from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'order-products', views.OrderProductViewSet)
router.register(r'fargo', views.FargoViewSet)
router.register(r'addresses', views.AddressViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
