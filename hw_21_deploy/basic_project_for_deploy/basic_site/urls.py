from django.urls import path
from basic_project_for_deploy import settings
from basic_site.views import update_user_profile, home, main_page_view, one_genre
from django.conf.urls.static import static

urlpatterns = [
	path('profile/', update_user_profile, name='user_profile_form'),
	path('main_page/', main_page_view, name='main_page'),
	path('home/', home, name='home'),
	path('genre/<int:genre_id>/', one_genre, name='one_genre'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
