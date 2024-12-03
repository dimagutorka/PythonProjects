from django.shortcuts import render, redirect, get_object_or_404
from basic_site.forms import UserProfileForm, UserForm, MovieForm
from django.contrib import messages
from basic_site.models import Genres, Movies


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
		form = MovieForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your movie has been created')

			return redirect('movie')


		else:
			return render(request, 'basic_site/movie_creation.html', {"form": form})



def home(request):
	return render(request, 'basic_site/home.html')


def genres_page_view(request):
	all_genres = Genres.objects.all()
	context = {'genres': all_genres}
	return render(request, 'basic_site/genres_page.html', context)


def genre_page_view(request, genre_id):
	one_genre = get_object_or_404(Genres, pk=genre_id)
	movies = one_genre.movies.all()
	context = {'movies': movies}

	return render(request, 'basic_site/genre_page.html', context)


def movie_page_view(request, movie_id):
	movie = Movies.objects.get(pk=movie_id)
	context = {'movie': movie}
	return render(request, 'basic_site/movie_page.html', context)