from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in ('GET', 'POST', 'PUT') and (request.user and request.user.is_authenticated):
			return True

		return bool(request.user and request.user.is_staff)
