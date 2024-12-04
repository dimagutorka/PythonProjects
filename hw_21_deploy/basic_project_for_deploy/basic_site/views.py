from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from basic_site.forms import UserProfileForm, UserForm, MovieForm, CommentForm, RateForm
from django.contrib import messages
from basic_site.models import Genres, Movies, Rate


def update_user_profile(request):
	if request.method == 'POST':
		form_user = UserForm(request.POST, instance=request.user)
		form_userprofile = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

		if form_user.is_valid() and form_userprofile.is_valid():
			print(request.FILES.get('avatar'))

			form_user.save()
			form_userprofile.save()
			messages.success(request, 'Your profile has been updated')

			return redirect('home')

	else:

		form_user = UserForm(instance=request.user)
		form_userprofile = UserProfileForm(instance=request.user.profile)

	return render(request, 'basic_site/update_user.html', {'form_user': form_user,
	                                                       'form_userprofile': form_userprofile})


def create_movie(request):
	if request.method == 'GET':
		form = MovieForm()
		return render(request, 'basic_site/movie_creation.html', {'form': form})

	if request.method == 'POST':
		form = MovieForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your movie has been created')

			return redirect('home')

		else:
			return render(request, 'basic_site/movie_creation.html', {"form": form})


def home(request):
	return render(request, 'basic_site/home.html')


def genres_page_view(request):
	all_genres = Genres.objects.all()
	# the_most_rated_movies = Movies.objects.order_by('-rates')[:3]

	context = {'genres': all_genres}
	return render(request, 'basic_site/genres_page.html', context)


def genre_page_view(request, genre_id):
	all_movies_in_genre = get_object_or_404(Genres, pk=genre_id)
	movies = all_movies_in_genre.movies.all()
	context = {'movies': movies}

	return render(request, 'basic_site/genre_page.html', context)


def movie_page_view(request, movie_id):
	movie = Movies.objects.get(pk=movie_id)
	avg_movie_rate = movie.rates.all().aggregate(Avg('rate'))['rate__avg']
	# This ['rate__avg'] is needed to retrieve the value from the dict
	comments = movie.comments.all().select_related('user')
	context = {'movie': movie,
	           'comments': comments,
	           'avg_movie_rate': avg_movie_rate}

	if request.method == 'GET':
		form = CommentForm()
		context['form'] = form
		return render(request, 'basic_site/movie_page.html', context)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.movie = movie
			comment.save()

			messages.success(request, message='Your comment has been added')
			return redirect('movie', movie_id=movie_id)

		else:
			context['form'] = form
			return render(request, 'basic_site/movie_page.html', context)


def rate_movie(request, movie_id):
	movie = get_object_or_404(Movies, pk=movie_id)
	user = request.user

	try:
		rate_instance = Rate.objects.get(user=user, movie=movie)
	except Rate.DoesNotExist:
		rate_instance = None

	form = RateForm(instance=rate_instance)

	if request.method == 'POST':
		form = RateForm(request.POST, instance=rate_instance)

		if form.is_valid():
			rate = form.save(commit=False)
			rate.user = user
			rate.movie = movie
			rate.save()

			return redirect('movie', movie_id=movie_id)

		else:
			return render(request, 'basic_site/rating.html', {'form': form, 'movie_id': movie.id})

	return render(request, 'basic_site/rating.html', {'form': form, 'movie_id': movie.id})





# If your template accesses the movie's genres:
# Copy code
# {% for genre in movie.genres.all %}
#     {{ genre.name }}
# {% endfor %}
# You can optimize this by prefetching genres:

# movie = Movies.objects.prefetch_related('genres').get(pk=movie_id