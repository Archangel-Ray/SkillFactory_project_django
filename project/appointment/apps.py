from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment'

    def ready(self):
        import appointment.signals

        from .tasks import send_mails
        from .scheduler import appointment_schedulers
        print('started')  # для отображения момента запуска периодической задачи

        appointment_schedulers.add_job(
            id='mail send',
            func=send_mails,
            trigger='interval',
            seconds=10,
        )
        appointment_schedulers.start()

        # запуск сервера без тестирования один раз:
        # python manage.py runserver 8010 --noreload
        # если внесены изменения автоматического перезапуска не будет
        # сервер надо перезапускать, чтоб изменения вошли в силу.
