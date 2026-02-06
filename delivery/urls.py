from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"delivery" , views.DeliveryModelViewSet)
router.register(r"delivery" , views.DeliveryAddressModelViewSet)
router.register(r"deliverymarketlog" , views.DeliveryMarketLogModelViewSet)
router.register(r"deliverygroup" , views.DeliveryGroupModelViewSet)
router.register(r"DeliveryWork" , views.DeliveryWorkModelViewSet)


urlpatterns = [
    path("",include(router.urls))
]


