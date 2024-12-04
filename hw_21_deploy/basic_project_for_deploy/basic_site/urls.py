from django.urls import path
from basic_project_for_deploy import settings
from basic_site.views import update_user_profile, home, genre_page_view, genres_page_view, movie_page_view, create_movie
from django.conf.urls.static import static

urlpatterns = [
	path('home/', home, name='home'),
	path('profile/', update_user_profile, name='user_profile_form'),
	path('genres/', genres_page_view, name='genres'),
	path('genre/<int:genre_id>/', genre_page_view, name='genre'),
	path('movie/<int:movie_id>', movie_page_view, name='movie'),
	path('movie_creation/', create_movie, name='movie_creation'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
