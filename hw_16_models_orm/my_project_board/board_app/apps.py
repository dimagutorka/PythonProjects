from django.apps import AppConfig


class BoardAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board_app'


    def ready(self):
        import board_app.signals
