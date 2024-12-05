from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
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


def genres_page_view(request):
	all_genres = Genres.objects.all()
	# the_most_rated_movies = Movies.objects.order_by('-rates')[:3] # CHECK !!!!

	context = {'genres': all_genres}
	return render(request, 'basic_site/genres_page.html', context)


def genre_page_view(request, genre_id):
	all_movies_in_genre = get_object_or_404(Genres, pk=genre_id)
	movies = all_movies_in_genre.movies.all()
	context = {'movies': movies}

	return render(request, 'basic_site/genre_page.html', context)


def movie_page_view(request, movie_id):
	movie = get_object_or_404(Movies, pk=movie_id)
	avg_movie_rate = movie.rates.all().aggregate(Avg('rate'))['rate__avg']
	comments = movie.comments.all().select_related('user')

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

	context = {'movie': movie,
	           'comments': comments,
	           'avg_movie_rate': avg_movie_rate,
	           'comment_form': comment_form,
	           'rate_form': rate_form}

	return render(request, 'basic_site/movie_page.html', context)


def cookie_test(request):
	response = HttpResponse('Set cookie')
	response.set_cookie('cookie_name', 'my_cookie')
	response.set_cookie('cookie_name1', 'my_cookie1')

	return render(request, 'basic_site/rating.html', {'response': response})


# def login_page(request):
# 	form = AuthenticationForm()
# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		user = authenticate(request, username=username, password=password)
#
# 		if user is None:
# 			context = {'error': 'Invalid username or password', 'form': form}
# 			return render(request, 'basic_site/login_page.html', {'form': form})
#
# 		response = redirect('home')
# 		response.set_cookie('username', username, max_age=10)
#
# 		login(request, user)
# 		return response
#
# 	return render(request, 'basic_site/login_page.html', {'form': form})


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


# If your template accesses the movie's genres:
# Copy code
# {% for genre in movie.genres.all %}
#     {{ genre.name }}
# {% endfor %}
# You can optimize this by prefetching genres:

# movie = Movies.objects.prefetch_related('genres').get(pk=movie_id