from django.conf import settings
from django.db.models.signals import post_save
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создания объекта письма с html
from datetime import datetime

from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from .models import Appointment


def notify_managers_appointment(sender, instance, created, **kwargs):
    """
    sender: модель
    instance: созданный объект модели
    created: есть в базе или нет
    """

    # получаем наш html
    html_content = render_to_string(
        'appointment_created.html',
        {
            'appointment': instance,
        }
    )

    # в конструкторе уже знакомые нам параметры, да? Называются правда немного по-другому, но суть та же.
    msg = EmailMultiAlternatives(
        subject=f'{instance.client_name} {instance.date.strftime("%Y-%m-%d")}',
        body=instance.message,  # это то же, что и message
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.DEFAULT_FROM_EMAIL],  # это то же, что и recipients_list
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()  # отсылаем


post_save.connect(notify_managers_appointment, sender=Appointment)


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        return redirect('appointments:make_appointment')
