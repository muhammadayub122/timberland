from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
      
    )
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def str(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(
        'auth.User',  # Reference to Django's default User model
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        
    )
    name = models.CharField(max_length=300)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def str(self):
        return self.name


class ComboProduct(models.Model):
    combo = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='combo_items',
        null=True,
 
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    
    )
    amount = models.PositiveIntegerField(default=1)

