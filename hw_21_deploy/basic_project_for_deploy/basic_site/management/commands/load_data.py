import requests
from django.core.management.base import BaseCommand
from basic_site.models import Movies, Genres


class Command(BaseCommand):
	help = "Load movies and genres into the database from TMDB API"

	token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MjVhODFiMjExZWQ1MmFjMTdhYmJhYWIyY2VjZDM5YSIsIm5iZiI6MTczMzQ3NTU0OC45NzYsInN1YiI6IjY3NTJiY2RjODBlNWI4ZjBhNzU2MzEzMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zX82V-5f3weDqX-4sTp4rvxY2YPyT7Z_AHdTLYYI2mI'
	headers = {"accept": "application/json", "Authorization": token}

	url_to_genres = "https://api.themoviedb.org/3/genre/movie/list?language=en"
	url_to_movies = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=7&sort_by=popularity.desc"

	def add_arguments(self, parser):
		parser.add_argument(
			'--task',
			choices=['load_genres', 'load_movies'],
			help="Specify which task to run: 'load_genres' or 'load_movies'. If not provided, both will run.")

	def handle(self, *args, **options):
		task = options['task']
		if task == 'load_genres':
			self.load_genres()
		elif task == 'load_movies':
			self.load_movies()
		else:
			self.load_genres()
			self.load_movies()

	def load_movies(self):
		img_size = '/w500'
		base_url = 'https://image.tmdb.org/t/p'
		r = requests.get(url=self.url_to_movies, headers=self.headers)

		for i in r.json()['results']:
			poster_path = base_url + img_size + i['poster_path']
			genres = i['genre_ids']

			movie = Movies.objects.create(
				title=i['title'],
				overview=i['overview'],
				release_date=i['release_date'],
				country=i['original_language'],
				poster=poster_path,
				adult=i['adult']
			)
			movie.save()

			r = requests.get(self.url_to_genres, headers=self.headers).json()['genres']
			for ids in r:
				if ids['id'] in genres:
					genre = Genres.objects.get(name=ids['name'])
					movie.genres.add(genre)

		self.stdout.write(self.style.SUCCESS('Movies loaded successfully'))

	def load_genres(self):
		r = requests.get(url=self.url_to_genres, headers=self.headers).json()['genres']
		for i in r:
			genre = Genres.objects.create(name=i['name'])
			genre.save()

		self.stdout.write(self.style.SUCCESS('Genres loaded successfully'))


	def load_users(self):


		self.stdout.write(self.style.SUCCESS('users loaded successfully'))