from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=100, unique=True)


class Product(models.Model):
    name_product = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# Create model Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
