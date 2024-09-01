from .models import Category, Product
# импортируем декоратор для перевода и класс настроек, от которого будем наследоваться
from modeltranslation.translator import register, TranslationOptions


# регистрируем наши модели для перевода
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    # указываем, какие именно поля надо переводить в виде кортежа
    fields = ('name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
