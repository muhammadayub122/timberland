from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/login/', TokenObtainPairView.as_view()),
    path('v1/token/refresh/', TokenRefreshView.as_view()),
]