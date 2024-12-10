from django.shortcuts import render
from my_site.models import *


def index(request):
	return render(request, 'my_site/index.html')
