from django.contrib import admin

from django.contrib import admin
from .models import Seller, SellerWalletLog

# Register your models here.




@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'phone', 'wallet', 'total_product_count', 'address')
    search_fields = ('name', 'phone', 'user__username')
    list_filter = ('wallet',)

    

@admin.register(SellerWalletLog)
class SellerWalletLogAdmin(admin.ModelAdmin):
    list_display = ('seller', 'amount', 'is_take', 'created_at')
    list_filter = ('is_take', 'created_at')
    date_hierarchy = 'created_at'
