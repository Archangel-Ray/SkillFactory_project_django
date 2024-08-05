from django.conf import settings
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создания объекта письма с html
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст

from appointment.models import Appointment


@receiver(post_save, sender=Appointment)
def notify_managers_appointment(sender, instance, created, **kwargs):
    """
    sender: модель
    instance: созданный объект модели
    created: есть в базе или нет
    """
    if created:
        new_subject = f'{instance.client_name} {instance.date.strftime("%Y-%m-%d")}',
    else:
        new_subject = f'Запись {instance.client_name} от {instance.date.strftime("%Y-%m-%d")} была изменена',

    # получаем наш html
    html_content = render_to_string(
        'appointment_created.html',
        {
            'appointment': instance,
        }
    )

    # в конструкторе уже знакомые нам параметры, да? Называются правда немного по-другому, но суть та же.
    msg = EmailMultiAlternatives(
        subject=new_subject,
        body=instance.message,  # это то же, что и message
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.DEFAULT_FROM_EMAIL],  # это то же, что и recipients_list
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()  # отсылаем
