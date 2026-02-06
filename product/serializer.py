from rest_framework .serializers import ModelSerializer
from .models import Category,Product,ComboProduct
from rest_framework.exceptions import ValidationError
class CategorySarialiser(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def validate_name (self, value):
        print(value) 
        if len(value) <= 3 :
            raise ValidationError("kategory nomi 3 tadan kam bo'lmasin")
        return value
    def validate_is_active(self,is_active):
        if is_active == False :
            raise ValidationError("Is activeni false qilma yaramas")
        return is_active

class ProductSerialiser(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
    def validate_price(self, price):
        if price <= 2000 :
            raise ValidationError("2000 dan ko'proq bo'sin")
        return price
    def validate_is_active(self,is_active):
        if is_active == False :
            raise ValidationError("Is activeni false qilma yaramas")
        return is_active
    def validate_name (self, value):
        print(value) 
        if len(value) <= 5 :
            raise ValidationError("product nomi 5 tadan kam bo'lmasin")
        return value
class ComboProductSerialier(ModelSerializer):

    class Meta:
        model = ComboProduct
        fields = '__all__'
    
    def validate_amount(self, amount):
        if amount <=0 :
            raise ValidationError("Bu Product savdoda yo'q")
        return 