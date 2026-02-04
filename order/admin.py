from django.contrib import admin
from .models import Order, OrderProduct, Fargo, Address


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "total_price", "status")
    list_filter = ("status",)
    inlines = (OrderProductInline, AddressInline)


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "quantity", "price")


@admin.register(Fargo)
class FargoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "fargo_status")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "address_name", "street", "home")


