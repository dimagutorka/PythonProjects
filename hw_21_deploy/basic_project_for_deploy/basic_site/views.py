from django.shortcuts import render, get_list_or_404
from basic_site.models import UserProfile
from django.contrib.auth.models import User


def home(request):
	# list_user = get_list_or_404(User)
	context = {"all_users": 111}
	return render(request, 'basic_site/home.html', context)