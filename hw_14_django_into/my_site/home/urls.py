from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
	path('home', views.home_view, name='home'),
	path('about', views.about_view, name='about'),
	path('contact_us', views.contact_view, name='contact_us'),
	re_path(r'^article/[0-9]{4}/[0-9]{1,2}/[\w-]+/$', views.articles_view)

]
