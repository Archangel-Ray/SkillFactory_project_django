"""
Документация по созданию пользовательских команд для manage.py
https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/
на русском
https://djangodoc.ru/3.2/howto/custom-management-commands/
"""

from django.core.management.base import BaseCommand

from simpleapp.models import Product


class Command(BaseCommand):
    help = 'Обнуляет количество всех товаров'

    def handle(self, *args, **options):
        for product in Product.objects.all():
            product.quantity = 0
            product.save()

            self.stdout.write(self.style.SUCCESS(f'у товара "{product}" поле количество = 0'))
