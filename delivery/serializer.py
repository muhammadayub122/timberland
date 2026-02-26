from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import (
    DeliveryGroup, Delivery, DeliveryAddress,
    DeliveryWork, DeliveryMarketLog
)

class DeliveryGroupSerializer(ModelSerializer):
    class Meta:
        model = DeliveryGroup
        fields = '__all__'


class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryAddressSerializer(ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = '__all__'


class DeliveryMarketLogSerializer(ModelSerializer):
    class Meta:
        model = DeliveryMarketLog
        fields = "__all__"

class DeliveryWorkSerializer(ModelSerializer):
    class Meta:
        model = DeliveryWork
        fields = '__all__'
