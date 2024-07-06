from django.db import models


class Order(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Staff(models.Model):
    pass


class ProductOrder(models.Model):
    pass
