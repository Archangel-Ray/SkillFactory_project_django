from django.db import models


class Order(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Staff(models.Model):
    full_name = models.CharField(max_length=255)  # текст с ограничением
    position = models.CharField(max_length=255)  # текст с ограничением
    labor_contract = models.IntegerField()  # целое число


class ProductOrder(models.Model):
    pass
