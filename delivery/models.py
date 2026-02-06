from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from user.models import User
class DeliveryGroup(models.Model):
    
    name = models.CharField(max_length=100, )
    group_type = models.CharField(max_length=50, blank=True,)
    message_id = models.BigIntegerField(null=True, blank=True, )
    topic_name = models.CharField(max_length=200, blank=True,)
    topic_id = models.IntegerField(null=True, blank=True, )

    created_at = models.DateTimeField(auto_now_add=True)

 
    def str(self):
        return self.name


class Delivery(models.Model):

    group = models.ForeignKey(
        DeliveryGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
      
    )

    user = models.ForeignKey(
        User,  
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
     
    )

    created_at = models.DateTimeField(default=timezone.now, verbose_name="Создан")
    working_status = models.CharField(
        max_length=50,
 
        choices=[
            ("new", "Новый"),
            ("in_progress", "В работе"),
            ("done", "Выполнен"),
            ("canceled", "Отменён"),
        ]
    )
    options_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0,)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, )

  
class DeliveryAddress(models.Model):
   
    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
    
    )
    address_name = models.CharField(max_length=300, )
    latitude = models.FloatField(null=True, blank=True,)
    longitude = models.FloatField(null=True, blank=True, )
    created_at = models.DateTimeField(auto_now_add=True)



    def str(self):
        return self.address_name[:60]


class DeliveryWork(models.Model):
    
    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
 
    )
    work_type = models.CharField(max_length=100, )
    work_link = models.CharField(blank=True, )
    created_at = models.DateTimeField(auto_now_add=True)


    def str(self):
        return f"{self.work_type} — {self.delivery}"


class DeliveryMarketLog(models.Model):

    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
    )
    market = models.CharField(max_length=100, )

    created_at = models.DateTimeField(auto_now_add=True)