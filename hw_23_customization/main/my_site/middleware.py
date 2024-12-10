from prometheus_client import Counter
from django.utils.deprecation import MiddlewareMixin


class CustomMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		response['Custom'] = 'Custom Value'
		return response


REQUEST_COUNT = Counter(
	'http_requests_total',
	'Total number of HTTP requests',
	['method', 'endpoint']
)


class RequestMetricsMiddleware(MiddlewareMixin):
	def process_request(self, request):
		REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
