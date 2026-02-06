from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class LeadStatus(models.Model):
    name = models.CharField(max_length=100)
    status = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,)

    def str(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    
    orders_count = models.PositiveIntegerField(default=0)
    returns_count = models.PositiveIntegerField(default=0)        
    lead = models.ForeignKey(LeadStatus, on_delete=models.SET_NULL, null=True, blank=True, )
    trek_number = models.CharField(max_length=100, blank=True)      
    custom_number = models.CharField(max_length=100, blank=True)   
    from_where = models.CharField(max_length=200, blank=True)     

    tags = models.ManyToManyField(Tag, blank=True, )

    def str(self):
        return f"Клиент {self.user.username if self.user else self.pk}"




class Favorite(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='favorites')
    product_id = models.CharField(max_length=100)              


    def str(self):
        return f"Избранное {self.client} — {self.product_id}"


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cart_items')
    product_id = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def str(self):
        return f"Корзина {self.client} — {self.product_id} ×{self.quantity}"


class DeliveryGroup(models.Model):
    group_id = models.CharField(max_length=100, blank=True)
    group_name = models.CharField(max_length=200)

    def __str__(self):
        return self.group_name


class Delivery(models.Model):
    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    orders_count = models.PositiveIntegerField(default=0)
    working_status = models.CharField(max_length=50, default='new')
    group = models.ForeignKey(DeliveryGroup, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')

    def __str__(self):
        return f"Delivery {self.id} - {self.working_status}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')

    def __str__(self):
        return f"Order {self.id} for {self.client}"


