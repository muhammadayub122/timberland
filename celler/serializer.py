#
from .models import Seller,SellerWalletLog
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

class SellerSerializer(ModelSerializer):
    class Meta:
        model=Seller
        fields='__all__'
        
    def validate_name(self,name):
        if name <= 4:
            raise ValidationError('ismiz kickina')
class SellerWalletLogSerializer(ModelSerializer):
    
         class Meta:
            model=SellerWalletLog
            fields='__all__'