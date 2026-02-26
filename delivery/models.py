from django.db import models
from django.utils import timezone
from user.models import User


class DeliveryGroup(models.Model):

    name = models.CharField(max_length=100)
    group_type = models.CharField(max_length=50, blank=True)
    message_number = models.BigIntegerField(null=True, blank=True)
    topic_name = models.CharField(max_length=200, blank=True)
    topic_number = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):

    group = models.ForeignKey(
        DeliveryGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deliveries"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deliveries"
    )

    created_at = models.DateTimeField(default=timezone.now)
    
    WORKING_STATUS_CHOICES = [
        ("new", "Новый"),
        ("in_progress", "В работе"),
        ("done", "Выполнен"),
        ("canceled", "Отменён"),
    ]

    working_status = models.CharField(
        max_length=50,
        choices=WORKING_STATUS_CHOICES,
        default="new"
    )

    options_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Delivery #{self.id}"


class DeliveryAddress(models.Model):

    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    address_name = models.CharField(max_length=300)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address_name[:60]


class DeliveryWork(models.Model):

    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        related_name="works"
    )

    work_type = models.CharField(max_length=100)
    work_link = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.work_type} — Delivery #{self.delivery.id}"


class DeliveryMarketLog(models.Model):

    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        related_name="market_logs"
    )

    market = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.market} — Delivery {self.delivery.id}"