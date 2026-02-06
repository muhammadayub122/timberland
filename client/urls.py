#
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'client',views.ClientModelViewSet,),

router.register(r'cart',views.CartModelViewSet),

router.register(r'tag',views.TagModelViewSet),

router.register(r'favourite',views.FavouriteModelViewSet),

router.register(r'leadstatus',views.LeadStatusModelViewSet),

urlpatterns = [
    path('',include (router.urls)),
]
