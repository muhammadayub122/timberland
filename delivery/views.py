from rest_framework.viewsets import ModelViewSet
from .serializer import DeliveryAddressSerializer,DeliveryGroupSerializer,DeliveryMarketLogSerializer,DeliverySerializer,DeliveryWorkSerializer
from .models import (
    DeliveryGroup, Delivery, DeliveryAddress,
    DeliveryWork, DeliveryMarketLog
)



class DeliveryGroupModelViewSet(ModelViewSet):
    queryset = DeliveryGroup.objects.all()
    serializer_class = DeliveryGroupSerializer

class DeliveryModelViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryAddressModelViewSet(ModelViewSet):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer


class DeliveryWorkModelViewSet(ModelViewSet):
    queryset = DeliveryWork.objects.all()
    serializer_class = DeliveryWorkSerializer

class DeliveryMarketLogModelViewSet(ModelViewSet):
    queryset = DeliveryMarketLog.objects.all()
    serializer_class = DeliveryMarketLog