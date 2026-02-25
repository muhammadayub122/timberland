from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Order, OrderProduct, Fargo, Address
from .serializer import (
    OrderSerializer, OrderCreateUpdateSerializer,
    OrderProductSerializer, FargoSerializer, AddressSerializer
)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related('products', 'address')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'payment_type', 'is_active']
    search_fields = ['client', 'delivery']
    ordering_fields = ['created_at', 'total_price']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return OrderCreateUpdateSerializer
        return OrderSerializer

  
    def update_status(self, request, pk=None):
        order = self.get_object()
        status_value = request.data.get('status')
        
        if status_value:
            order.status = status_value
            order.save()
            return Response({
                'message': f'Status updated to {order.get_status_display()}',
                'status': order.status
            })
        return Response(
            {'error': 'status field required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    
    def by_status(self, request):
        
        status_param = request.query_params.get('status')
        if status_param:
            orders = self.queryset.filter(status=status_param)
            serializer = self.get_serializer(orders, many=True)
            return Response(serializer.data)
        return Response(
            {'error': 'status parameter required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )


class OrderProductViewSet(viewsets.ModelViewSet):
  
    queryset = OrderProduct.objects.all().select_related('order')
    serializer_class = OrderProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order', 'product_id']


class FargoViewSet(viewsets.ModelViewSet):
    
    queryset = Fargo.objects.all()
    serializer_class = FargoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['fargo_status']
    search_fields = ['name']


    def update_status(self, request, pk=None):
        
        fargo = self.get_object()
        status_value = request.data.get('fargo_status')
        
        if status_value:
            fargo.fargo_status = status_value
            fargo.save()
            return Response({
                'message': f'Status updated to {fargo.get_fargo_status_display()}',
                'status': fargo.fargo_status
            })
        return Response(
            {'error': 'fargo_status field required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )


class AddressViewSet(viewsets.ModelViewSet):
   
    queryset = Address.objects.all().select_related('order')
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['in_tashkent', 'order']
    search_fields = ['address_name', 'street']