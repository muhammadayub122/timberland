from django.db import models

# Create your models here.





class User(models.Model):
    class Role(models.TextChoices):
        USER = 'USER', 'user'
        ADMIN = 'ADMIN', 'admin'
        CELLER = 'CELLER', 'celler'
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    middel_name = models.CharField(max_length=155)
    user_name = models.CharField(max_length=155)
    age = models.PositiveIntegerField(default=1)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='user/',blank=True,null=True)
    address = models.CharField(max_length=255)


