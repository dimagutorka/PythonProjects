from django.urls import path

from basic_project_for_deploy import settings
from basic_site.views import update_user_profile, home
from django.conf.urls.static import static

urlpatterns = [
	path('profile/', update_user_profile, name='user_profile_form'),
	path('home/', home, name='home'),


]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
