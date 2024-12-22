from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from basic_site.models import Genres, Movies, Rate, WatchLater, FriendsList
from basic_site.forms import (UserProfileForm, UserForm, MovieForm, CommentForm,
                              RateForm, CSVFileForm, RegistrationForm, LoginForm, AddToWatchLater, AddFriend,
                              AcceptFriend)
from basic_site.tasks import from_csvfile_to_bd


# TODO-7: Add validation in forms form unathorized user who click rate/watch latter buttons
# TODO-6: add field avatar + last_updated/created to comment section on a movie page
# TODO-5: Refactor views (too long)
@login_required(login_url='/login_page/')
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

	return render(request, 'basic_site/update_user.html', {
		'form_user': form_user,
		'form_userprofile': form_userprofile})


@login_required(login_url='/login_page/')
def create_movie(request):
	form = MovieForm()
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
	num_comments = (Movies.objects.prefetch_related('genres')
	                .annotate(num_comments=Count('comments')).order_by('-num_comments'))

	return render(request, 'basic_site/genres_page.html',
	              {'genres': all_genres, 'num_comments': num_comments})


def genre_page_view(request, genre_id):
	genre = get_object_or_404(Genres, pk=genre_id)
	all_movies_in_genre = genre.movies.values('id', 'title')
	context = {'movies': all_movies_in_genre}

	return render(request, 'basic_site/genre_page.html', context)


def handle_comment_submission(request, movie):
	comment_form = CommentForm(request.POST)

	if comment_form.is_valid():
		comment = comment_form.save(commit=False)
		comment.user = request.user
		comment.movie = movie
		comment.save()
		messages.success(request, message='Your comment has been added')
	return comment_form


def handle_rate_submission(request, movie):
	rate_form = RateForm(request.POST)

	if rate_form.is_valid():
		rate = rate_form.save(commit=False)
		rate.user = request.user
		rate.movie = movie
		rate.save()
		messages.success(request, message='Your rate has been added')
	return rate_form


def handle_watch_later_list(request, movie):
	watch_later_form = AddToWatchLater(request.POST)

	if watch_later_form.is_valid():
		form = watch_later_form.save(commit=False)
		form.user = request.user
		form.movie = movie
		form.save()
	return watch_later_form


def update_recently_viewed(request, movie_id):
	recently_viewed = request.session.get("recently_viewed", [])

	if movie_id in recently_viewed:
		recently_viewed.remove(movie_id)
		recently_viewed.insert(0, movie_id)

	elif movie_id not in recently_viewed:
		recently_viewed.insert(0, movie_id)

	if len(recently_viewed) > 5:
		recently_viewed.pop()

	request.session["recently_viewed"] = recently_viewed
	request.session.modified = True

	return Movies.objects.filter(id__in=recently_viewed)


# TODO-9: Make users' profiles which post comments active Other users can
#  click on their avatar/nickname and go to their profile
def movie_page_view(request, movie_id):
	movie = get_object_or_404(Movies, pk=movie_id)
	avg_movie_rate = movie.rates.all().aggregate(Avg('rate'))['rate__avg']
	genres_in_movie = movie.genres.all()
	comments = movie.comments.select_related('user').all()

	rate_instance = Rate.objects.filter(user=request.user, movie=movie).first()

	# Empty forms
	watch_later_form = AddToWatchLater()
	comment_form = CommentForm()
	rate_form = RateForm(instance=rate_instance)

	if request.method == 'POST':
		if 'comment_submit' in request.POST:
			comment_form = handle_comment_submission(request, movie)
			return redirect('movie', movie_id=movie_id)

		elif 'rate_submit' in request.POST and request.user.is_authenticated:
			rate_form = handle_rate_submission(request, movie)
			return redirect('movie', movie_id=movie_id)

		# if movies + user exists else:
		elif 'watch_later_submit' in request.POST:
			watch_later_form = handle_watch_later_list(request, movie)
			return redirect('movie', movie_id=movie_id)

	recently_viewed_movies = update_recently_viewed(request, movie_id)

	context = {
		'movie': movie,
		'comments': comments,
		'avg_movie_rate': avg_movie_rate,
		'comment_form': comment_form,
		'rate_form': rate_form,
		"recently_viewed": recently_viewed_movies,
		"genres_in_movie": genres_in_movie,
		"watch_later_form": watch_later_form,
	}

	return render(request, 'basic_site/movie_page.html', context)


# move to the utils.py
def some_filters(request):
	num_comments = Movies.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')
	avg_rating = Movies.objects.annotate(avg_rating=Avg('rates', default=1)).order_by('-avg_rating')

	contex = {'num_comments': num_comments,
	          'avg_rating': avg_rating}

	return render(request, 'basic_site/home.html', contex)


@login_required(login_url='/login_page/')
def create_movie_via_csv(request):
	if request.method == 'POST':
		form = CSVFileForm(request.POST, request.FILES)
		context = {"form": form}

		if form.is_valid():
			csv_file_instance = form.save()
			messages.success(request, 'Your movie has been created')

			filename = csv_file_instance.csv_filename.name
			result = from_csvfile_to_bd.delay(filename)

			context['task_id'] = result.task_id
	# return redirect('home')
	else:
		form = CSVFileForm()
		context = {"form": form}
	return render(request, 'basic_site/movie_creation_via_csv.html', context)


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
	form = LoginForm(request.POST or None)
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(request, username=username, password=password)

		if user is not None:
			request.session.flush()
			login(request, user)
			messages.success(request, f'Welcome back, {user.username}!')
			return redirect('home')
		else:
			messages.error(request, 'Invalid username or password.')
			return redirect('login_page')

	return render(request, 'basic_site/login_page.html', {"form": form})


@login_required(login_url='/login_page/')
def logout_view(request):
	logout(request)
	return redirect('home')


# TODO-4: Add movies you can like (think about ideas how it could be implemented)
def home(request):
	username = request.session['username'] if 'username' in request.session else 'Guest'

	movies = Movies.objects.all()
	the_most_discussed_movies = movies.annotate(num_comments=Count('comments')).order_by('-num_comments')[:5]
	the_most_rated_movies = movies.order_by('-average_rating')[:5]
	recently_released = movies.order_by('-release_date')[:5]

	return render(request, 'basic_site/home.html', {
		'username': username,
		'the_most_discussed_movies': the_most_discussed_movies,
		'most_rated_movies': the_most_rated_movies,
		'recently_released': recently_released})


@login_required(login_url='/login_page/')
def profile(request, user_id):
	request_user_id = request.user
	user = User.objects.get(id=user_id)
	user_data = User.objects.select_related('profile').get(id=user_id)
	friend = FriendsList.objects.filter(user_id=request_user_id, friend_id=user_id).first()

	most_rated = user.rates.all().order_by('-rate')[:3]
	least_rated = user.rates.all().order_by('rate')[:3]

	friend_ids = FriendsList.objects.values_list('friend_id', flat=True).filter(user=request_user_id)

	if request.method == 'POST':

		if 'add_friend' in request.POST:
			user_fried_form = AddFriend(request.POST)
			if user_fried_form.is_valid():
				form = user_fried_form.save(commit=False)
				form.user = request_user_id
				form.friend = user
				form.save()

		if 'delete_friend' in request.POST:
			FriendsList.objects.get(friend_id=user_id).delete()

		return redirect('profile', user_id=user_id)

	context = {'user_data': user_data,
	           'most_rated': most_rated,
	           'least_rated': least_rated,
	           'user_id': user_id,
	           'friend_ids': friend_ids,
	           'friend': friend}

	return render(request, 'basic_site/user_profile.html', context)


@login_required(login_url='/login_page/')
def friends_list(request):
	request_user_id = request.user
	friend_ids = FriendsList.objects.values_list('user_id', flat=True).filter(friend_id=request_user_id,
	                                                                          is_friend=False)
	friend_requests = User.objects.filter(id__in=friend_ids)

	if request.method == 'POST':
		friend_id = request.POST.get('user_id', None)
		if "accept_friend" in request.POST:
			friend_entry = get_object_or_404(FriendsList, user_id=friend_id, friend_id=request_user_id)
			if not friend_entry.is_friend:
				friend_entry.is_friend = True
				friend_entry.save()
				messages.success(request, 'Friend accepted')
			else:
				messages.warning(request, 'You already accepted')

		elif "decline_friend" in request.POST:
			declined_friend = FriendsList.objects.filter(user_id=friend_id, friend_id=request_user_id)
			if declined_friend.exists():
				declined_friend.delete()
				messages.info(request, "Friend request declined.")
			else:
				messages.warning(request, 'You already declined')

		return redirect('friends_list')

	return render(request, 'basic_site/friends_list.html', {'friend_requests': friend_requests})




# ПОПРОБОВАТЬ ПЕРЕСВЯЗАТЬ ВСЕ ЧЕРЕЗ ТАБЛИЦУ ЮЗЕРОВ
# usr = User.objects.get(id=1) | usr.friends