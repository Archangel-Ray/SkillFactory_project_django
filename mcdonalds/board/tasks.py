from celery import shared_task
import time


@shared_task
def hello():
    time.sleep(10)
    print("Тут СкиллФактори посылает Хелло на Ворлд! (с восклицательным знаком, обязательно)")


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i + 1)
