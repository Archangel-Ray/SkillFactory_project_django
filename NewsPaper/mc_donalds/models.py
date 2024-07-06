from django.db import models


class Order(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Staff(models.Model):
    # константы для списка должностей
    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'

    # список должностей
    POSITIONS = [
        (director, 'Директор'),
        (admin, 'Администратор'),
        (cook, 'Повар'),
        (cashier, 'Кассир'),
        (cleaner, 'Уборщик')
    ]

    full_name = models.CharField(max_length=255)  # текст с ограничением
    position = models.CharField(max_length=2,  # текст с ограничением
                                choices=POSITIONS,  # прикреплённый список
                                default=cashier)  # значение по умолчанию
    labor_contract = models.IntegerField()  # целое число


class ProductOrder(models.Model):
    pass
