from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import JsonResponse
from .tasks import send_mail_task, test_task


def index(request):
	"""work effectively for foreign keys"""
	query_set = Book.objects.select_related('author')


def many_to_many(request):
	"""for complicated relations """
	query_set = Book.objects.prefetch_related('author')


@cache_page(60 * 15)
def my_view(request):
	return HttpResponse('Hello World!')


def get_books(request):
	books = cache.get('books')
	if not books:
		books = Book.objects.all()
		cache.set('books', books, 60 * 15)
	return HttpResponse(books)


def send_email_view(request):
	subject = 'TEST EMAIL'
	message = 'TEST MESSAGE'
	from_email = 'dgutorka@gmail.com'
	recipient_list = [from_email]

	send_mail_task(subject, message, from_email, recipient_list)
	return JsonResponse({'status': 'email sent'})



def index1(request):
	test_task()
	return JsonResponse({'status': 'email sent'})

