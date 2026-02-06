from django.shortcuts import render
from .serializer import ClientSerializer,TagSerializer,CartSerializer,LeadStatusSerializer,FavouriteSerializer
from .models import LeadStatus,Client,Cart,Tag,Favorite
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class ClientModelViewSet(ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
class  TagModelViewSet(ModelViewSet):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer
class CartModelViewSet(ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
class LeadStatusModelViewSet(ModelViewSet):
    queryset=LeadStatus.objects.all()
    serializer_class=LeadStatusSerializer
class FavouriteModelViewSet(ModelViewSet):
    queryset=Favorite.objects.all()
    serializer_class=FavouriteSerializer

    