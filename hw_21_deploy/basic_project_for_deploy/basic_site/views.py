from django.contrib.auth.decorators import login_required

from basic_site.models import Genres, Movies, Rate
from basic_site.forms import UserProfileForm, UserForm, MovieForm, CommentForm, RateForm, CSVFileForm, RegistrationForm, LoginForm
from basic_site.tasks import from_csvfile_to_bd
from django.db.models import Avg, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.cache import cache
from django.contrib.auth import login, authenticate, logout


@login_required(login_url='no_account')
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
		a = request.FILES['poster']
		print(f'Request: {a}')

		if form.is_valid():
			form.save()
			messages.success(request, 'Your movie has been created')

			return redirect('home')

		else:
			return render(request, 'basic_site/movie_creation.html', {"form": form})


# @cache_page(60*1)
def genres_page_view(request):
	all_genres = cache.get('genres')

	if all_genres is None:
		all_genres = Genres.objects.prefetch_related('movies')
		cache.set('genres', all_genres, timeout=3600)
		print('hit the db')
	else:
		print('hit the cache')

	num_comments = (Movies.objects.prefetch_related('genres')
	                .annotate(num_comments=Count('comments'))
	                .order_by('-num_comments'))
	the_most_rated_movies = Movies.objects.order_by('-average_rating')[:3]  # CHECK !!!!

	context = {
		'genres': all_genres,
		'num_comments': num_comments,
		'the_most_rated_movies': the_most_rated_movies
	}
	return render(request, 'basic_site/genres_page.html', context)


def genre_page_view(request, genre_id):
	genre = get_object_or_404(Genres, pk=genre_id)
	all_movies_in_genre = genre.movies.values('id', 'title')
	context = {'movies': all_movies_in_genre}

	return render(request, 'basic_site/genre_page.html', context)


def movie_page_view(request, movie_id):
	movie = get_object_or_404(Movies, pk=movie_id)
	avg_movie_rate = movie.rates.all().aggregate(Avg('rate'))['rate__avg']
	genres_in_movie = movie.genres.all()
	comments = movie.comments.select_related('user').all()

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


# move to the utils.py
def some_filters(request):
	num_comments = Movies.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')
	avg_rating = Movies.objects.annotate(avg_rating=Avg('rates', default=1)).order_by('-avg_rating')

	contex = {'num_comments': num_comments,
	          'avg_rating': avg_rating}

	return render(request, 'basic_site/home.html', contex)


def create_movie_via_csv(request):
	if request.method == 'POST':
		form = CSVFileForm(request.POST, request.FILES)

		if form.is_valid():
			csv_file_instance = form.save()
			messages.success(request, 'Your movie has been created')

			filename = csv_file_instance.csv_filename.name
			from_csvfile_to_bd.delay(filename)

			return redirect('home')
	else:
		form = CSVFileForm()
	return render(request, 'basic_site/movie_creation_via_csv.html', {"form": form})


def registration_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			request.session['username'] = user.username

			return redirect('home')

	else:
		form = RegistrationForm()
	return render(request, 'basic_site/registration_page.html', {'form': form})


def login_view(request):

	form = LoginForm()
	context = {'form': form}

	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(request, username=username, password=password)

		if user is None:
			context = {'form': form, 'error': 'Invalid username or password.'}

		request.session['username'] = username
		login(request, user)

		return redirect('home')

	return render(request, 'basic_site/login_page.html', context)


def logout_view(request):
	logout(request)
	request.session.flush()
	return redirect('home')


def home(request):
	username = 'Guest'
	if 'username' in request.session:
		username = request.session['username']

	return render(request, 'basic_site/home.html', {'username': username})


# HW 22 PS It's inactive because I already have full-fledged login/logout system, it's just for HW

# def login_page_for_hw(request):
# 	if request.method == 'POST':
# 		name = request.POST.get('name')
# 		age = request.POST.get('age')
#
# 		response = redirect('home')
# 		response.set_cookie('name', name, max_age=30)
# 		request.session['age'] = age
#
# 		return response
#
# 	return render(request, 'basic_site/login_page.html')
#
#
# def login_page_for_hw(request):
# 	response = redirect('home')
# 	response.delete_cookie('name')
# 	request.session.flush()
# 	return response

#
# def home(request):
#
# 	username = request.COOKIES.get('name')
# 	age = request.session.get('age')
#
# 	if not username or not age:
# 		return redirect('login')
#
# 	response = HttpResponse(f'Hello, {username}! you\'re age is {age}')
# 	response.set_cookie('name', username, max_age=30)
#
# 	return response
