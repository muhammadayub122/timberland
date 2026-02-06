from rest_framework.serializers import ModelSerializer
from .models import OrderProduct, Order, Address




class OrderProductSerializer(ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = '__all__'




class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'




class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'













