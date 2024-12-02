from django.contrib import admin
from django.urls import path, include
from .views import send_email_view, index1

urlpatterns = [
	path('send_email/', send_email_view, name='send_email'),
	path('test/', index1, name='test'),



]