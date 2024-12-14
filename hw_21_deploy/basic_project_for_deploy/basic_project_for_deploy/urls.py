from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from basic_site.api import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basic_site.urls')),
    path('api/', api.urls),
    path(r'^celery-progress/', include('celery_progress.urls')),

] + debug_toolbar_urls()
