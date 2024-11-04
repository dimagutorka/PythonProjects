from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
	return HttpResponse("Welcome on home page")


def about_view(request):
	return HttpResponse("The page about us")


def contact_view(request):
	return HttpResponse("Contact us page")


def articles_view(request):
	return HttpResponse(f'OK - 200')