from rest_framework import serializers
from .models import Order, OrderProduct, Fargo, Address, OrderStatus


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = '__all__'
        read_only_fields = ['id']


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    
    products = OrderProductSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)
    status_display = serializers.SerializerMethodField()
    payment_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def get_status_display(self, obj):
        
        return obj.get_status_display()

    def get_payment_type_display(self, obj):
        
        return obj.get_payment_type_display()


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    
    products = OrderProductSerializer(many=True, required=False)
    address = AddressSerializer(required=False)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        products_data = validated_data.pop('products', [])
        address_data = validated_data.pop('address', None)
        
       
        order = Order.objects.create(**validated_data)
        
        
        for product_data in products_data:
            OrderProduct.objects.create(order=order, **product_data)
        
       
        if address_data:
            Address.objects.create(order=order, **address_data)
        
        return order

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products', [])
        address_data = validated_data.pop('address', None)
        
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        
        if products_data:
            instance.products.all().delete()
            for product_data in products_data:
                OrderProduct.objects.create(order=instance, **product_data)
        
        
        if address_data:
            Address.objects.update_or_create(order=instance, defaults=address_data)
        
        return instance


class FargoSerializer(serializers.ModelSerializer):
    
    fargo_status_display = serializers.SerializerMethodField()

    class Meta:
        model = Fargo
        fields = '__all__'
        read_only_fields = ['id']

    def get_fargo_status_display(self, obj):
        return obj.get_fargo_status_display()


class OrderStatusUpdateSerializer(serializers.Serializer):
    
    status = serializers.ChoiceField(choices=OrderStatus.choices)