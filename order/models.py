from django.db import models
import uuid
# Create your models here.





class OrderStatus(models.TextChoices):
    CREATED = 'created', 'Buyurtma yaratildi'
    CONFIRMING = 'confirming', 'Buyurtma tasdiqlanish jarayonida'
    PREPARING = 'preparing', 'Kuryer buyurtmani tayyorlamoqda'
    SENT_TO_FARGO = 'sent_to_fargo', 'Buyurtma fargo punktga topshirildi'
    DELIVERED = 'delivered', 'Buyurtma mijozga topshirildi'
    RETURNED = 'returned', 'Buyurtma qaytarildi'
    AT_FARGO = 'at_fargo', 'Buyurtma fargo punktida'
    TO_REGION = 'to_region', 'Viloyatga yuborilmoqda'
    REGION_RECEIVED = 'region_received', 'Viloyat punktga topshirildi'
    TO_CLIENT = 'to_client', 'Mijozga yuborilmoqda'
    FAILED_CALL = 'failed_call', 'Kuryer mijoz bilan boglana olmadi'






class PaymentType(models.TextChoices):
    CASH = 'cash', 'Cash'
    CARD = 'card', 'Card'
    CASH_CARD = 'cash_card', 'Cash / Card'
    MERCHANT = 'merchant', 'Merchant'








class Fargo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    fargo_status = models.CharField(
        max_length=30,
        choices=OrderStatus.choices,
        default=OrderStatus.CREATED
    )

    def __str__(self):
        return self.name







class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    client = models.CharField(max_length=255)
    delivery = models.CharField(max_length=255)

    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(
        max_length=30,
        choices=OrderStatus.choices,
        default=OrderStatus.CREATED
    )

    payment_type = models.CharField(
        max_length=20,
        choices=PaymentType.choices
    )

    is_send_fargo = models.BooleanField(default=False)

    fargo = models.ForeignKey(
        Fargo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)









class OrderProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='products'
    )

    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order} - {self.product_id}"







class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='address'
    )

    in_tashkent = models.BooleanField(default=True)

    address_name = models.CharField(max_length=255)

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    street = models.CharField(max_length=255)
    home = models.CharField(max_length=20)
    apartment = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.address_name









