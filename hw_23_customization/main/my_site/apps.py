from django.apps import AppConfig


class MySiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_site'

    def ready(self):
        from my_site import signals