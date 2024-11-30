from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from datetime import datetime

contacts = [
	{'first_name': 'dima', 'last_name': 'franko', 'email': 'dimafranko@gmail.com', 'phone': "3808275328", 'date': datetime.now()},
	{'first_name': 'Nadya', 'last_name': 'Shevchenko', 'email': 'shevchenko@gmail.com', 'date': datetime.now()},
	{'first_name': 'Taras', 'last_name': 'Bulba', 'email': 'Bulba@gmail.com', 'phone': "3930476235", 'date': datetime.now()},
	{'first_name': 'Olga', 'last_name': 'Kravchyk', 'email': 'Olga@gmail.com', 'phone': "3934576235", 'date': datetime.now()}
]

services = [
	{'service': 'dima', 'price': 100, 'is_avaliable': False, 'age': 14},
	{'service': 'Nadya', 'price': 75, 'is_avaliable': False, 'age': 23},
	{'service': 'Taras', 'price': 150, 'is_avaliable': True, 'age': 20},
	{'service': 'Olga', 'price': 10, 'is_avaliable': True, 'age': 24}
]

about_company = ("Founded in  2000, our company has grown from a small startup into a "
                 "trusted leader in the industry sector. With a commitment to innovation and excellence, "
                 "we have consistently delivered top-quality products and services to our customers.")


def about(request):
	template = loader.get_template('main/about.html')
	return HttpResponse(template.render({'description': about_company}, request))


def home(request):
	template = loader.get_template('main/home.html')
	return HttpResponse(template.render({'description': about_company}, request))


class ContactView(TemplateView):
	template_name = 'main/contacts.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['contacts'] = contacts
		return context


class ServiceView(TemplateView):
	template_name = 'main/service.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['services'] = services
		return context
