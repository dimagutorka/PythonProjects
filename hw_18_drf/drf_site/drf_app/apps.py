from django.apps import AppConfig


class DrfAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drf_app'

    def ready(self):
        from drf_app import signals
