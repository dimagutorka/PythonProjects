from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class CacheMoviesListMiddleWare(MiddlewareMixin):

	def process_request(self, request):
		if request.user.is_anonymous and request.path == '/movie_pave/':
			cached_response = cache.get('movies_list')
			if cached_response:
				return HttpResponse(f'Here\'s your cached movies list: {cached_response}')

	def process_response(self, request, response):
		if request.user.is_anonymous and request.path == '/movie_pave/' and response.status_code == 200:
			if 'movies_list' not in cache:
				cache.set('movies_list', response.content, timeout=300)
		return response
