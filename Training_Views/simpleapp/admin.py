from django.contrib import admin
# импортируем модель админ-панели (вспоминаем модуль про переопределение стандартных админ-инструментов)
from modeltranslation.admin import TranslationAdmin
from .models import Category, Product


# напишем уже знакомую нам функцию обнуления товара на складе
def nullfy_quantity(modeladmin, request, queryset):
    # все аргументы уже должны быть вам знакомы, самые нужные из них это
    # request — объект хранящий информацию о запросе и
    # queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)


# описание для более понятного представления в админ панели задаётся, как будто это объект
nullfy_quantity.short_description = 'Обнулить товары'


# создаём новый класс для представления товаров в админке
class ProductAdmin(admin.ModelAdmin, TranslationAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('name', 'price', 'on_stock', 'quantity')  # оставляем только имя и цену товара
    list_filter = ('price', 'quantity', 'name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category__name')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список


# Регистрируем модели для перевода в админ-панели
class CategoryAdmin(TranslationAdmin):
    model = Category


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# admin.site.unregister(Product) # разрегистрируем наши товары
