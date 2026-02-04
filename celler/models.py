from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Seller(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='seller_profile'
    )
    name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    latitude = models.FloatField(null=True, blank=True)   
    longitude = models.FloatField(null=True, blank=True) 
    address = models.TextField(blank=True)
    wallet = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_product_count = models.PositiveIntegerField(default=0) 
    def str(self):
        return self.name or self.user.username or f"Продавец {self.pk}"


class SellerWalletLog(models.Model):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name='wallet_logs'
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    is_take = models.BooleanField(default=False)  
   
    created_at = models.DateTimeField(default=timezone.now)

    
    description = models.CharField(max_length=255, blank=True) 
    order = models.ForeignKey('client.Order', null=True, blank=True, on_delete=models.SET_NULL)
    transaction_type = models.CharField(
        max_length=50,
        choices=[
            ('deposit', 'Deposit'),
            ('withdrawal', 'Withdrawal')
        ]
    )

    def str(self):
        sign = "-" if self.is_take else "+"
        return f"{sign}{self.amount} для {self.seller} ({self.created_at:%Y-%m-%d})"