from my_site.models import *


def categories(request):
	category = Category.objects.all().first()
	return {'categories': category}


def products(request):
	product = Product.objects.all().first()
	request_headers = request.headers
	return {'products': product,
	        'request_headers': request_headers}