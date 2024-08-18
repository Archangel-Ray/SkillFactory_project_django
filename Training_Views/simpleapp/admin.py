from django.contrib import admin

from .models import Category, Product


# создаём новый класс для представления товаров в админке
class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('name', 'price', 'on_stock')  # оставляем только имя и цену товара
    list_filter = ('price', 'quantity', 'name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category__name')  # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# admin.site.unregister(Product) # разрегистрируем наши товары
