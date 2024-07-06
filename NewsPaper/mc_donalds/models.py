from django.db import models


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


class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)  # дата и время оформления заказа
    time_out = models.DateTimeField(null=True)  # дата и время выдачи заказа
    cost = models.FloatField(default=0.0)  # общая стоимость заказа
    pickup = models.BooleanField(default=False)  # True, если заказ нужно собрать для самовывоза
    complete = models.BooleanField(default=False)  # True, если заказ уже выполнен
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)  # связь с Сотрудником

    products = models.ManyToManyField(Product, through = 'ProductOrder')  # связь "Товар"-"Заказ"


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # связь с товаром
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # связь с заказом
    amount = models.IntegerField(default=1)  # количество товаров
