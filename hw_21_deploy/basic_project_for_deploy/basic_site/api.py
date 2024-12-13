from typing import List
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Query
from basic_site.models import Movies, Genres
from basic_site.schemas import MovieSchema, GenreSchema, MovieCreateSchema, Error, MovieUpdateSchema, GenreCreateSchema, MovieFilterSchema

api = NinjaAPI(version="1.0.0")


@api.get("movies/", response=list[MovieSchema])
def get_movies_with_filters(request, sort_by: str = Query("title"), title_by_word: str = Query(None)):
	movies = Movies.objects.all().order_by(sort_by)
	if title_by_word:
		movies = movies.filter(title__icontains=title_by_word)
	return movies


@api.get("movies/{id}/", response=MovieSchema)
def get_movie(request, id: int):
	return get_object_or_404(Movies, id=id)


@api.post("movies/", response={200: MovieSchema, 404: Error})
def create_movie(request, movie: MovieCreateSchema):
	all_genres = Genres.objects.all().values_list("id", flat=True)

	if movie.genres:
		for genre in movie.genres:
			if genre not in all_genres:
				return 404, {"message": "genre does not exist"}

	movie_data = movie.model_dump()
	movie_creation = Movies.objects.create(
		title=movie_data["title"],
		overview=movie_data["overview"],
		release_date=movie_data["release_date"],
		country=movie_data["country"],
	)

	movie_creation.genres.set(movie_data["genres"])
	movie_creation.save()
	return movie_creation


@api.put("movies/{id}/update/", response={200: MovieSchema, 404: Error})
def update_movie(request, id: int, movie: MovieUpdateSchema):
	movie_get = get_object_or_404(Movies, id=id)
	movie_data = movie.model_dump()

	if movie_get:
		for key, value in movie_data.items():
			if isinstance(value, list) and value is not None:
				related_field = getattr(movie_get, key)

				if related_field and hasattr(related_field, 'set'):
					related_field.set(value)

			elif value is not None:
				setattr(movie_get, key, value)

		movie_get.save()
		return movie_get


@api.delete("movies/{id}/delete/")
def delete_movie(request, id: int):
	movie_get = get_object_or_404(Movies, id=id)
	movie_get.delete()
	return {"success": f"Movie with id {id} has been deleted successfully."}


@api.get("genres/", response=list[GenreSchema])
def get_genres(request):
	return Genres.objects.all()


@api.get("genres/{id}/", response=GenreSchema)
def get_genre(request, id: int):
	return get_object_or_404(Genres, id=id)


@api.post('genres/', response=GenreSchema)
def create_genre(request, genre: GenreCreateSchema):
	genre_data = genre.model_dump()
	genre_creation = Genres.objects.create(name=genre_data["name"])
	return genre_creation


@api.delete("genres/{id}/delete/", response=GenreSchema)
def delete_genre(request, id: int):
	genre_get = get_object_or_404(Genres, id=id)
	genre_get.delete()
	return genre_get
