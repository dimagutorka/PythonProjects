from django.contrib import admin
from django.urls import path, include
from my_site.views import *

urlpatterns = [
    path('index/', index, name='index'),
]