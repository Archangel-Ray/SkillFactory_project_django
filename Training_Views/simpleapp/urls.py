from django.urls import path
from django.views.decorators.cache import cache_page

# Импортируем созданное нами представление
from .views import ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    # path — означает путь.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', ProductsList.as_view(), name='product_list'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    # ссылка на представление создание продукта
    path('create/', ProductCreate.as_view(), name='product_create'),
    # ссылка на представление редактирования продукта
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    # ссылка на представление удаление продукта
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
]
