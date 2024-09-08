"""
документация по классам представлений
https://www.django-rest-framework.org/api-guide/generic-views/
"""
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
        return Response({'title': 'Дженнифер Лоуренс'})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()  # считывание всех данных из модели
#     serializer_class = WomenSerializer  # назначение сериализатора
