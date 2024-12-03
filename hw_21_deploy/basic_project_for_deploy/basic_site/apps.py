from django.apps import AppConfig


class BasicSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basic_site'

    # def ready(self):
    #     import basic_site.signals
