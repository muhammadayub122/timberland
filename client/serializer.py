

from .models import  Client,Cart,Tag,Favorite,LeadStatus
from rest_framework.serializers import ModelSerializer



class ClientSerializer(ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'
class CartSerializer(ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
class TagSerializer(ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'
class FavouriteSerializer(ModelSerializer):
    class Meta:
        model=Favorite
        fields='__all__'
class LeadStatusSerializer(ModelSerializer):
    class Meta:
        model=LeadStatus
        fields='__all__'
