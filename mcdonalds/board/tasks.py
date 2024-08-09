from celery import shared_task

from .models import Order


@shared_task
def complete_order(oid):
    order = Order.objects.get(pk=oid)
    order.complete = True
    order.save()


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
