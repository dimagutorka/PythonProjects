from django.urls import path
from social.views import *

urlpatterns = [
	path('friends/', friends_list, name='friends'),

]
