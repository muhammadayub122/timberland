from rest_framework.viewsets import ModelViewSet
from .serializer import OrderSerializer,  AddressSerializer, OrderProductSerializer 
from .models import Order, OrderProduct, Address
# Create your views here.




class OrderApiiview(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()




class OrderProductApiiview(ModelViewSet):
    serializer_class = OrderProductSerializer
    queryset = OrderProduct.objects.all()





class AddressApiiview(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

