"""
Настройка собственных команд для запуска от "manage.py"
описание от Джанго:
https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
создать файл с командами по пути
приложение/management/commands/файл_запуска.py

Описание настроек Django APScheduler:
https://pypi.org/project/django-apscheduler/
варианты исполнения:
1. Используйте пользовательскую команду управления Django для запуска отдельного планировщика в его собственном
   выделенном процессе (рекомендуется - см. runapscheduler.py пример ниже);
2. Внедрите свою собственную логику удаленной обработки, чтобы гарантировать, что один DjangoJobStore может
   использоваться всеми рабочими процессами веб-сервера скоординированным и синхронизированным образом
   (в большинстве случаев это может не стоить дополнительных усилий и повышенной сложности);
3. Выберите альтернативную библиотеку обработки задач, которая поддерживает взаимодействие между процессами
   с использованием какого-либо общего посредника обмена сообщениями, такого как Redis, RabbitMQ, Amazon SQS и т.п.
   (популярные варианты смотрите здесь: https://djangopackages.org/grids/g/workers-queues-tasks/).
"""
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

logger = logging.getLogger(__name__)


def my_job():
    # Your job processing logic here...
    print('СкиллФактори красавцы!')


# Декоратор `close_old_connections` гарантирует, что соединения с базой данных, которые стали непригодны
# для использования или устарели, закрываются до и после выполнения вашего задания. Вы должны использовать это
# для упаковки любых запланированных вами заданий, которые каким-либо образом обращаются к базе данных Django.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    Это задание удаляет из базы данных записи выполнения заданий APScheduler старше max_age.
    Это помогает предотвратить заполнение базы данных старыми историческими записями,
    которые не являются дольше полезно.

    :param max_age: Максимальный срок хранения исторических записей выполнения заданий.
                    По умолчанию 7 дней.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Каждые 10 секунд
            id="my_job",  # Идентификатор, присвоенный каждому заданию, ДОЛЖЕН быть уникальным.
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Полночь понедельника, перед началом следующей рабочей недели.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
