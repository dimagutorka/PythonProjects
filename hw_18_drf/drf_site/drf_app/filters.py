import django_filters
from drf_app.models import Book


class BookFilter(django_filters.FilterSet):
	title__icontains = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

	class Meta:
		model = Book
		fields = ['publication_year', 'title', 'genre']