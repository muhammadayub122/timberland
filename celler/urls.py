#

from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()

router.register(r'seller',views.SellerModelView,)
router.register(r'sellerwalletlog',views.SellerWalletLogModelView,)
urlpatterns = [
    path('',include(router.urls))
]
