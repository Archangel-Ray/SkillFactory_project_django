from celery import shared_task
import time

from .models import Order


@shared_task
def complete_order(oid):
    order = Order.objects.get(pk=oid)
    order.complete = True
    order.save()

# запуск задач
# celery -A mcdonalds worker -l INFO --pool=solo
