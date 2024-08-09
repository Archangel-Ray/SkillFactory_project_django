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

Для запуска периодических задач на Windows запустите в разных окнах терминала:
$ celery -A PROJECT worker -l INFO
и
$ celery -A PROJECT beat -l INFO
"""
