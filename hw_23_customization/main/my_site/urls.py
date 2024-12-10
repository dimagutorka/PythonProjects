from django.contrib import admin
from django.urls import path, include
from prometheus_client import metrics

from my_site.views import *

urlpatterns = [
    path('index/', index, name='index'),
    # path('registration/', registration_view, name='register'),
    path('home/', home, name='home'),
    path('test/', MyFormView.as_view(), name='test'),
    path('metrics/', metrics_view, name='metrics'),
]
