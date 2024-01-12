from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class ApiUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    USER_TYPE_CHOICES = (
        ('supplier', 'Поставщик'),
        ('consumer', 'Потребитель'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)



class Warehouse(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
