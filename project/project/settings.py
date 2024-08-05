"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1rc1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-37tav6v#pjy5_g)z#_+4i#i_(&!2_ij%)&yyjal7hg2j8szfvr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'appointment.apps.AppointmentConfig',
    'django.contrib.sites',
    'django_apscheduler',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
# изменяем настройки так, как это было в документации
# https://docs.allauth.org/en/latest/installation/quickstart.html#post-installation


SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Добавьте промежуточное программное обеспечение учетной записи:
    "allauth.account.middleware.AccountMiddleware",
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # Для каждого провайдера на основе OAuth либо добавьте ``SocialApp``
        # (приложение ``sociaaccount``), содержащее требуемый клиент
        # учетные данные или перечислите их здесь:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый

# ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user,
# иными словами, это всё то что идёт до собаки
EMAIL_HOST_USER = open('G:/Python_projects/all_secret_codes_are_here/Yandex email/login.txt').read()
# пароль от почты
EMAIL_HOST_PASSWORD = open('G:/Python_projects/all_secret_codes_are_here/Yandex email/password.txt').read()

# Яндекс использует ssl, подробнее о том, что это, почитайте в
# дополнительных источниках, но включать его здесь обязательно
EMAIL_USE_SSL = True

# эл.почта с которой будет производиться отправка
DEFAULT_FROM_EMAIL = open('G:/Python_projects/all_secret_codes_are_here/Yandex email/email.txt').read()

AUTHENTICATION_BACKENDS = [
    # Необходимо войти в систему по имени пользователя в администраторе Django, независимо от `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # специальные методы аутентификации `allauth`, такие как вход по электронной почте.
    'allauth.account.auth_backends.AuthenticationBackend',
]
# настройка для django-apscheduler
# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# настройка для django-apscheduler
# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше,
# но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds
