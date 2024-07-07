from datetime import datetime

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

    def get_last_name(self):
        return self.full_name.split()[0]


class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)  # дата и время оформления заказа
    time_out = models.DateTimeField(null=True)  # дата и время выдачи заказа
    cost = models.FloatField(default=0.0)  # общая стоимость заказа
    pickup = models.BooleanField(default=False)  # True, если заказ нужно собрать для самовывоза
    complete = models.BooleanField(default=False)  # True, если заказ уже выполнен
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='orders')  # связь с Сотрудником

    products = models.ManyToManyField(Product, through='ProductOrder')  # связь "Товар"-"Заказ"

    # завершение заказа
    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    # время выполнения заказа
    def get_duration(self):
        if self.complete:  # если завершён, возвращаем разность начала и завершения
            return (self.time_out - self.time_in).total_seconds()
        else:  # если ещё нет, то сколько времи прошло до этого момента
            return (datetime.now() - self.time_in).total_seconds()


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # связь с товаром
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # связь с заказом
    _amount = models.IntegerField(default=1, db_column='amount')  # количество товаров

    # возвращает общее количество
    @property
    def amount(self):
        return self._amount

    # проверка на отрицательное значение
    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()

    # общая стоимость
    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount