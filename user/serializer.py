from rest_framework .serializers import ModelSerializer
from .models import User
from rest_framework.exceptions import ValidationError
class UserSarialiser(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def validate_first_name(self, first_name):
        if first_name <= 3 :
            raise ValidationError("Isim 3 ta xariflardan ko'p bo'lsin ")
        return first_name
    def validate_age(self, age):
        if age <= 14 :
            raise ValidationError("Siz kichgina bo'lasiz kotta bo'lib kirin yoki oyizzi chaqirin")
        return age
    def validate_phone_number(self, phone_number):
        if len(phone_number) >= 12 :
            raise ValidationError("Ortiqcha raqam mumkin emas ")
        return 
    