import os
from celery import Celery
from celery.schedules import crontab

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

# запуск очистки
app.conf.beat_schedule = {
    'clear_board_every_minute': {
        'task': 'board.tasks.clear_old',
        'schedule': crontab(),  # каждую минуту
    },
}

# таблица задания периодов
# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#crontab-schedules

# # пример
# app.conf.beat_schedule = {
#     'запустит в понедельник в восемь утра': {
#         'task': 'задача',
#         'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
#         'args': (args),
#     },
# }
# # https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#periodic-tasks

"""
запуск периодических задач на Windows в разных окнах терминала:
$ celery -A mcdonalds worker -l INFO --pool=solo
и
$ celery -A mcdonalds beat -l INFO
"""
