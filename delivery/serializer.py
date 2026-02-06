from rest_framework .serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import (
    DeliveryGroup, Delivery, DeliveryAddress,
    DeliveryWork, DeliveryMarketLog
)

class DeliveryGroupSerializer(ModelSerializer):
    model = DeliveryGroup
    fields = '__all__'


class DeliverySerializer(ModelSerializer):
    model = Delivery
    fields = '__all__'



class DeliveryAddressSerializer(ModelSerializer):
    model = DeliveryAddress
    fields = '__all__'


class DeliveryMarketLogSerializer(ModelSerializer):
    model = DeliveryMarketLog
    fields = '__all__'

class DeliveryWorkSerializer(ModelSerializer):
    model = DeliveryWork
    fields = '__all__'
