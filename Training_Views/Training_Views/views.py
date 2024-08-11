from django.shortcuts import render
from django.views.decorators.cache import cache_page # импортируем декоратор для кэширования отдельного представления


@cache_page(60 * 15)
# в аргументы к декоратору передаём количество секунд, которые хотим, чтобы страница держалась в кэше.
# Внимание! Пока страница находится в кэше, изменения, происходящие на ней, учитываться не будут!
def main(request):
    return render(request, 'flatpages/default.html')
