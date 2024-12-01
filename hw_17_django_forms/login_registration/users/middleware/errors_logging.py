import logging
from django.http import HttpResponseNotFound, HttpResponseServerError

logger_404 = logging.getLogger('error_logger_404')
logger_500 = logging.getLogger('error_logger_500')


class ErrorsLoggingMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)

		if response.status_code == 404:
			logger_404.warning(
				f"404 Error: Path={request.path}, Method={request.method}, "
				f"Referer={request.META.get('HTTP_REFERER', 'No referer')}, "
			)

		return response


	def process_exception(self, request, exception):
		logger_500.error(
			f'500 Error {request.path}'
			f'Method={request.method}'
			f'Exception={str(exception)}',
			exc_info=exception
		)

		return HttpResponseServerError("An internal server error occurred.")

