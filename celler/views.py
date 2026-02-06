from django.shortcuts import render
from .serializer import SellerSerializer,SellerWalletLogSerializer
from .models import Seller,SellerWalletLog
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class SellerModelView(ModelViewSet):
    queryset=Seller.objects.all()
    serializer_class=SellerSerializer
class SellerWalletLogModelView(ModelViewSet):
    queryset=SellerWalletLog.objects.all()
    serializer_class=SellerWalletLogSerializer
    