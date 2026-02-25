from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from .serializer import UserSerializer
# Create your views here.




class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]  
        return [IsAuthenticated()]  