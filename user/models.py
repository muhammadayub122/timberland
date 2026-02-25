from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'USER', 'user'
        ADMIN = 'ADMIN', 'admin'
        CELLER = 'CELLER', 'celler'
    
    
    middel_name = models.CharField(max_length=155, blank=True, null=True)
    age = models.PositiveIntegerField(default=1)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='user/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    
    REQUIRED_FIELDS = ['email', 'phone_number']
    
    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"