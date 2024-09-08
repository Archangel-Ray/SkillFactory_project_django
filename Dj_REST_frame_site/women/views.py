"""
документация по классам представлений
https://www.django-rest-framework.org/api-guide/generic-views/
"""
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):  # наследуемся от базового класса
    # обработчик GET запросов
    def get(self, request):
        list_of_all_data = Women.objects.all().values()
        return Response({'posts': list(list_of_all_data)})

    # обработчик POST запросов
    def post(self, request):
        new_post = Women.objects.create(  # создаёт новую запись в базе и сохраняет в переменную
            # в соответствующие поля модели заносим данные полученные из запроса
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        # возвращает сохранённую переменную преобразованную в словарь
        # в которой сохранена только что созданная запись модели
        return Response({'post': model_to_dict(new_post)})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()  # считывание всех данных из модели
#     serializer_class = WomenSerializer  # назначение сериализатора
