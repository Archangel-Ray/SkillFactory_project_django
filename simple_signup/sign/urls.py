from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import BaseRegisterView

urlpatterns = [
    # идентификация и аутентификация
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    # отключение аутентификации
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    # регистрация
    path('signup/',
         BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
]
