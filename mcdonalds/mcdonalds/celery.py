import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcdonalds.settings')
# связываем настройки Django с настройками Celery через переменную окружения

app = Celery('mcdonalds')  # экземпляр Celery
app.config_from_object('django.conf:settings', namespace='CELERY')
# Устанавливаем файл конфигурации. Указываем пространство имён, чтобы Celery сам находил все необходимые
# настройки в общем конфигурационном файле settings.py. Он их будет искать по шаблону «CELERY_***».

app.autodiscover_tasks()  # автоматически искать задания в файлах tasks.py каждого приложения проекта

app.conf.beat_schedule = {
    'print_every_5_seconds': {  # периодическая задача
        'task': 'board.tasks.printer',  # задача которая должна выполняться
        'schedule': 20,  # период запуска
        'args': (5,),  # аргументы для выполняемой задачи
    },
}

"""
запуск периодических задач на Windows в разных окнах терминала:
$ celery -A mcdonalds worker -l INFO --pool=solo
и
$ celery -A mcdonalds beat -l INFO
"""
