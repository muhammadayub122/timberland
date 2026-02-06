from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"product" , views.ProductModelViewSet)
router.register(r"category" , views.CategoryModelViewSet)
router.register(r"comboproduct" , views.ComboProductModelViewSet)


urlpatterns = [
    path("",include(router.urls))
]


