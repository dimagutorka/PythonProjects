from django.contrib import admin
from django.urls import path
from basic_site.views import home


urlpatterns = [
	path('home/', home, name='home')
]
