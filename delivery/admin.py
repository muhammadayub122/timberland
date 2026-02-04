from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    DeliveryGroup, Delivery, DeliveryAddress,
    DeliveryWork, DeliveryMarketLog
)

admin.site.register(DeliveryGroup)
admin.site.register(Delivery)



admin.site.register(DeliveryAddress)


admin.site.register(DeliveryWork)


admin.site.register(DeliveryMarketLog)