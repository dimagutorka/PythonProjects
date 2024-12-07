from email.policy import default

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.db.models import Avg, Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from basic_site.forms import UserProfileForm, UserForm, MovieForm, CommentForm, RateForm
from django.contrib import messages
from basic_site.models import Genres, Movies, Rate, UserProfile


def update_user_profile(request):
	if request.method == 'POST':
		form_user = UserForm(request.POST, instance=request.user)
		form_userprofile = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

		if form_user.is_valid() and form_userprofile.is_valid():
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


def genres_page_view(request):
	all_genres = Genres.objects.prefetch_related('movies')
	num_comments = Movies.objects.prefetch_related('genres').annotate(num_comments=Count('comments')).order_by('-num_comments')
	the_most_rated_movies = Movies.objects.order_by('-average_rating')[:3] # CHECK !!!!

	context = {'genres': all_genres,
	           'num_comments': num_comments,
	           'the_most_rated_movies': the_most_rated_movies}
	return render(request, 'basic_site/genres_page.html', context)


def genre_page_view(request, genre_id):
	all_movies_in_genre = get_object_or_404(Genres, pk=genre_id)
	movies = all_movies_in_genre.movies.all()
	context = {'movies': movies}

	return render(request, 'basic_site/genre_page.html', context)


def movie_page_view(request, movie_id):
	movie = get_object_or_404(Movies, pk=movie_id)
	avg_movie_rate = movie.rates.all().aggregate(Avg('rate'))['rate__avg']
	genres_in_movie = movie.genres.all()
	comments = movie.comments.all().annotate()

	rate_instance = Rate.objects.filter(user=request.user, movie=movie).first()
	rate_form = RateForm(instance=rate_instance)
	comment_form = CommentForm()

	if request.method == 'POST':
		if 'comment_submit' in request.POST:
			comment_form = CommentForm(request.POST)

			if comment_form.is_valid():
				comment = comment_form.save(commit=False)
				comment.user = request.user
				comment.movie = movie
				comment.save()
				messages.success(request, message='Your comment has been added')
				return redirect('movie', movie_id=movie_id)

		elif 'rate_submit' in request.POST:
			rate_form = RateForm(request.POST, instance=rate_instance)

			if rate_form.is_valid():
				rate = rate_form.save(commit=False)
				rate.user = request.user
				rate.movie = movie
				rate.save()
				messages.success(request, message='Your rate has been added')
				return redirect('movie', movie_id=movie_id)

	recently_view_products = None

	# Recently movies
	if "recently_viewed" in request.session:

		movies = Movies.objects.filter(id__in=request.session["recently_viewed"])
		recently_view_products = sorted(movies, key=lambda x: request.session["recently_viewed"].index(x.id))

		if movie_id in request.session["recently_viewed"]:
			request.session["recently_viewed"].remove(movie_id)
			request.session["recently_viewed"].insert(0, movie_id)

		elif movie_id not in request.session["recently_viewed"]:
			request.session["recently_viewed"].insert(0, movie_id)

		if len(request.session["recently_viewed"]) >= 6:
			request.session["recently_viewed"].pop()

	else:
		request.session["recently_viewed"] = [movie_id]

	request.session.modified = True

	context = {'movie': movie,
	           'comments': comments,
	           'avg_movie_rate': avg_movie_rate,
	           'comment_form': comment_form,
	           'rate_form': rate_form,
	           "recently_viewed": recently_view_products,
	           "genres_in_movie": genres_in_movie
	           }

	return render(request, 'basic_site/movie_page.html', context)


def login_page(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		age = request.POST.get('age')

		response = redirect('home')
		response.set_cookie('name', name, max_age=30)
		request.session['age'] = age

		return response

	return render(request, 'basic_site/login_page.html')


def home(request):
	username = request.COOKIES.get('name')
	age = request.session.get('age')

	if not username or not age:
		return redirect('login')

	response = HttpResponse(f'Hello, {username}! you\'re age is {age}')
	response.set_cookie('name', username, max_age=30)

	return response


def logout_page(request):
	response = redirect('home')
	response.delete_cookie('name')
	request.session.flush()
	return response


def some_filters(request):
	num_comments = Movies.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')
	avg_rating = Movies.objects.annotate(avg_rating=Avg('rates', default=1)).order_by('-avg_rating')

	contex = {'num_comments': num_comments,
	          'avg_rating': avg_rating}


	return render(request, 'basic_site/home.html', contex)


