from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView

from my_site.models import *
from my_site.forms import *
from django.contrib import messages
from django.contrib.auth.models import User

from prometheus_client import generate_latest


def metrics_view(request):
	return HttpResponse(generate_latest(), content_type='text/plain')


def index(request):
	return render(request, 'my_site/index.html')


def home(request):
	return HttpResponse('HOME')


def registration_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Account created successfully')
			return redirect('home')
	else:
		form = RegisterForm()
	return render(request, 'my_site/registration_page.html', {'form': form})


class MyFormView(FormView):
	template_name = 'my_site/test_form.html'
	form_class = TestForm
	success_url = '/home/'

	def form_valid(self, form):
		user = User.objects.get(id=2)
		ff = form.save(commit=False)
		ff.user = user
		ff.save()
		return redirect(self.get_success_url())
