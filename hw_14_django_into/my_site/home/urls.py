from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
	path('', views.home_view, name='home'),
	path('home', views.home_view, name='home'),
	path('about', views.about_view, name='about'),
	path('contact_us', views.contact_view, name='contact_us'),
	re_path(r'^post/(?P<id>[0-9]+)/$', views.post_view, name='post'),
	re_path(r'^profile/(?P<username>[a-zA-Z]+)/$', views.profile_view, name='profile'),
	re_path(r'^event/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.event_view, name='event'),

]



