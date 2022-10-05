from pyexpat import model
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.CharField(max_length=200)
    is_per_unit = models.BooleanField(default=False)

class Farm(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=200)
    products = models.ManyToManyField(Product)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    number = models.IntegerField()
    postal_code = models.IntegerField()


