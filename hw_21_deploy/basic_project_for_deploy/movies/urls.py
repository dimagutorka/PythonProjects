from django.urls import path
from movies.views import *


urlpatterns = [
	path('genres/', genres_page_view, name='genres'),
	path('genre/<int:genre_id>/', genre_page_view, name='genre'),
	path('movie/<int:movie_id>', movie_page_view, name='movie'),
	path('movie/create/', create_movie, name='movie_create'),
	path('movies/import/', create_movie_via_csv, name='movie_import'),

]

