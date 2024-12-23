from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from core.api import api

urlpatterns = [
	              path(r'^celery-progress/', include('celery_progress.urls')),
	              path('admin/', admin.site.urls),
	              path('api/', api.urls),
	              path('users', include('users.urls')),
	              path('movies', include('movies.urls')),
	              path('social', include('social.urls')),
	              path('', include('core.urls')),

              ] + debug_toolbar_urls()
