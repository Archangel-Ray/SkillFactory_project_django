from celery import shared_task
import time


@shared_task
def hello():
    time.sleep(10)
    print("Тут СкиллФактори посылает Хелло на Ворлд! (с восклицательным знаком, обязательно)")
