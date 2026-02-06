from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerialiser,CategorySarialiser,ComboProductSerialier
from .models import Product,ComboProduct,Category


# Category list va create
class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySarialiser

class ComboProductModelViewSet(ModelViewSet):
    queryset = ComboProduct.objects.all()
    serializer_class = ComboProductSerialier
