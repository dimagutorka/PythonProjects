from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import Http404


def home_view(request):
	return HttpResponse("Welcome on home page")


def about_view(request):
	return HttpResponse("The page about us")


def contact_view(request):
	return HttpResponse("Contact us page")


def articles_view(request):
	return HttpResponse(f'OK - 200')


def post_view(request, id):
	return HttpResponse(f'You\'re watching post with - {id} id')


def profile_view(request, username):
	return HttpResponse(f'You\'re watching post of user - {username}')


def event_view(request, year, month, day):
	date = datetime.datetime(int(year), int(month), int(day))
	return HttpResponse(f'The date of the event is {date.strftime("%B %d, %Y")}')



