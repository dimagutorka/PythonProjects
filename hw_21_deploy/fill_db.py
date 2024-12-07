all_genres = Genres.objects.all()
url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MjVhODFiMjExZWQ1MmFjMTdhYmJhYWIyY2VjZDM5YSIsIm5iZiI6MTczMzQ3NTU0OC45NzYsInN1YiI6IjY3NTJiY2RjODBlNWI4ZjBhNzU2MzEzMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zX82V-5f3weDqX-4sTp4rvxY2YPyT7Z_AHdTLYYI2mI'
headers = {"accept": "application/json",
           "Authorization": token}

img_size = '/w500'
base_url = 'https://image.tmdb.org/t/p'

r = requests.get(url=url, headers=headers)

for i in r.json()['results']:
	poster_path = base_url + img_size + i['poster_path']
	movie = Movies.objects.create(
		title=i['title'],
		overview=i['overview'],
		release_date=i['release_date'],
		country=i['original_language'],
		poster=poster_path,
		adult=i['adult']
	)
	movie.save()


