from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [  # перечисление полей которые будут отображаться для редактирования
            'name',
            'description',
            'quantity',
            'category',
            'price',
        ]
