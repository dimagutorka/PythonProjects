import logging
from django.utils.timezone import now
from django.http import HttpResponseForbidden


logger = logging.getLogger('access_logger')


class ProtectedPageAccessMiddleWare:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not request.user.is_authenticated and self.is_protected_page(request):
			self.log_access_attempt(request)
			return HttpResponseForbidden("You are not authorized to access this page.")

		response = self.get_response(request)
		return response

	def is_protected_page(self, request):
		protected_page = ['/logout', '/profile', '/change_password', '/profile_update']

		for path in protected_page:
			if request.path.startswith(path):
				return True
			return False

	def log_access_attempt(self, request):
		logger.warning(
			f"Unauthorized access attempt: Path={request.path}, "
			f"User-Agent={request.META.get('HTTP_USER_AGENT', 'unknown')}, "
			f"Time={now().isoformat()}"
		)
