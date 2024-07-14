from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter

from .models import Product, Category


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
    # настройка поля фильтрации по конкретному значение
    category_name_one_field = ModelChoiceFilter(
        # имя поля в модели
        field_name='category',
        # список который будет отображаться в выпадающем списке
        queryset=Category.objects.all(),
        # название поля, которое будет отображаться
        label='Категория товара',
        # пустое поле в выпадающем списке
        empty_label='любая'
    )

    # настройка поля фильтрации по нескольким значениям
    category_name_more_field = ModelMultipleChoiceFilter(
        # имя поля в модели
        field_name='category',
        # список который будет отображаться в списке для сортировки
        queryset=Category.objects.all(),
        # название поля, которое будет отображаться
        label='Категория товара',
        # True - "И"; по умолчанию = False - "ИЛИ"
        conjoined=False
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Product
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'name': ['icontains'],
            # количество товаров должно быть больше или равно
            'quantity': ['gt'],
            'price': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],
            'category': ['exact'],  # по списку значение полей
        }
