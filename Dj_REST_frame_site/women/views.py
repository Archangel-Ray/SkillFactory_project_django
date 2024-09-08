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
        return Response({'title': 'Анджелина Джоли'})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()  # считывание всех данных из модели
#     serializer_class = WomenSerializer  # назначение сериализатора
