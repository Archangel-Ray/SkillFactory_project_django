import time
from datetime import datetime, timedelta, timezone

from celery import shared_task

from .models import Order


@shared_task
def complete_order(oid):
    order = Order.objects.get(pk=oid)
    order.complete = True
    order.save()


@shared_task
def clear_old():
    """
    Очистка от старых заказов
    """
    old_orders = Order.objects.all().exclude(time_in__gt=datetime.now(timezone.utc) - timedelta(minutes=5))
    old_orders.delete()


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i + 1)


"""
# Инициализация ВОРКЕРА
$ celery -A mcdonalds worker -l INFO --pool=solo
Селери приложить макдоналдса к воркеру, выводить в консоль: информацию
(в отделённых воспринимать независимо в одном потоке - это для Винды)
-A (application)  - приложение, дальше имя приложения
-l значение: INFO - что выводить в консоль
--concurrency=10  - количество процессов
-B                - запуска периодические задачи

запуск периодических задач на Windows в разных окнах терминала:
$ celery -A mcdonalds worker -l INFO --pool=solo
и
$ celery -A mcdonalds beat -l INFO
"""
