from django.urls import path
from main.views import home, about, ContactView, ServiceView

urlpatterns = [
	path('home/', home, name='home'),
	path('about/', about, name='about'),
	path('contacts/', ContactView.as_view(), name='contacts'),
	path('service/', ServiceView.as_view(), name='service')
]