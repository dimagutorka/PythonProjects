from basic_project_for_deploy import settings
from django.conf.urls.static import static

from django.urls import path
from core.views import *


urlpatterns = [
	path('home/', home, name='home'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

