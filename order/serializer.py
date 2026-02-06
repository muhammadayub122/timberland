<<<<<<< HEAD
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













=======
#
>>>>>>> 5b3ee4819a418d6f604816fe563dcf9c88bb9cab
