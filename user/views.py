from rest_framework.viewsets import ModelViewSet
from .serializer import UserSarialiser
from .models import User


# Category list va create
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSarialiser