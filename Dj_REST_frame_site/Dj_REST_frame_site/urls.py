"""
URL configuration for Dj_REST_frame_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers  # генератор путей

from women.views import *

# создаётся объект, который будет формировать текущие пути относительно представления
# документация https://www.django-rest-framework.org/api-guide/routers/
# собственные https://www.django-rest-framework.org/api-guide/routers/#custom-routers
# router = routers.DefaultRouter()  # возвращает пути если использовать без указания префикса
# регистрация представления в роутере
# router.register(
#     r'women',  # префикс маршрута
#     WomenViewSet,  # класс представления
#     basename='женщины',  # префикс для имени маршрута. если в представлении нет queryset, то имя обязательно
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    # подключение авторизации и аутентификации
    # документация https://www.django-rest-framework.org/api-guide/authentication/
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # подключение всех путей роутера
    # path('api/v1/', include(router.urls)),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
]
