from django.urls import path
from basic_project_for_deploy import settings
from basic_site.views import *
from django.conf.urls.static import static

urlpatterns = [
	path('home/', home, name='home'),
	path('profile/', update_user_profile, name='user_profile_form'),
	path('genres/', genres_page_view, name='genres'),
	path('genre/<int:genre_id>/', genre_page_view, name='genre'),
	path('movie/<int:movie_id>', movie_page_view, name='movie'),
	path('movie_creation/', create_movie, name='movie_creation'),
	path('login/', login_page, name='login'),
	path('logout/', logout_page, name='logout'),
	path('filters/', some_filters, name='filter'),
	path('movie_pave/', movie_page1, name='movie_pave'),
	path('test_celery/', test_celery, name='test_celery'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
