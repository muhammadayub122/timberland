from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Client, DeliveryGroup, Delivery, Favorite,
    Cart, Order, Tag, LeadStatus
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'orders_count', 'returns_count', 'lead', 'from_where')
    search_fields = ('userusername', 'userfirst_name', 'trek_number')
    list_filter = ('lead',)
    raw_id_fields = ('user', 'lead')


admin.site.register(DeliveryGroup)


admin.site.register(Delivery)


admin.site.register(Order)


admin.site.register(Cart)

admin.site.register(Favorite)


admin.site.register(Tag)

admin.site.register(LeadStatus)
