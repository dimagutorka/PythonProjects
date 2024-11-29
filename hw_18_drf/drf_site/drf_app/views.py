from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from drf_app.filters import BookFilter
from drf_app.models import Book
from drf_app.permissions import IsAdminOrReadOnly
from drf_app.serializers import BookSerializer
from rest_framework import viewsets


class BookListPagination(PageNumberPagination):
	page_size = 50
	page_size_query_param = 'page_size'
	max_page_size = 2


class BookList(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	pagination_class = BookListPagination
	permission_classes = [IsAdminOrReadOnly]
	authentication_classes = [TokenAuthentication]
	filter_backends = [DjangoFilterBackend]
	filterset_class = BookFilter
