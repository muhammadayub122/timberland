from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    DeliveryGroup, Delivery, DeliveryAddress,
    DeliveryWork, DeliveryMarketLog
)

class DeliveryGroupAdmin(admin.ModelAdmin):
    fields = ('name', 'group_type', 'topic_name', 'message_number', 'topic_number')
    list_display = ('name', 'group_type', 'topic_name', 'created_at')

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'working_status', 'user', 'group', 'created_at', 'total_cost')
    list_filter = ('working_status', 'created_at')
    search_fields = ('user__email', 'group__name')

class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'delivery', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('address_name',)

class DeliveryWorkAdmin(admin.ModelAdmin):
    list_display = ('work_type', 'delivery', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('work_type',)

class DeliveryMarketLogAdmin(admin.ModelAdmin):
    list_display = ('market', 'delivery', 'created_at')
    list_filter = ('market', 'created_at')

admin.site.register(DeliveryGroup, DeliveryGroupAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryAddress, DeliveryAddressAdmin)
admin.site.register(DeliveryWork, DeliveryWorkAdmin)
admin.site.register(DeliveryMarketLog, DeliveryMarketLogAdmin)