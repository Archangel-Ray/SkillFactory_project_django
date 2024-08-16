from django.apps import AppConfig


class ApplicationTemplateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{app_name}}'
