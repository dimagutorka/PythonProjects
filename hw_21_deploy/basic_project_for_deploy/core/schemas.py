from typing import List, Optional
from ninja import ModelSchema, Schema, FilterSchema
from core.models import Movies, Genres
from datetime import date


class GenreSchema(ModelSchema):
	class Meta:
		model = Genres
		fields = ('id', 'name')


class GenreCreateSchema(Schema):
	name: str


class MovieSchema(ModelSchema):
	genres: List[GenreSchema] | None = None

	class Meta:
		model = Movies
		fields = ('id', 'title', 'overview', 'release_date', 'country', 'genres', 'adult', 'average_rating')


class MovieCreateSchema(Schema):
	title: str
	overview: str
	release_date: date = None
	country: str = 'Not specified'
	genres: List[int]


class MovieUpdateSchema(Schema):
	title: str = None
	overview: str = None
	genres: List[int]


class MovieFilterSchema(FilterSchema):
	title: Optional[str]
	overview: Optional[str]
	release_date: Optional[date] | None = None
	country: Optional[str] | str = 'Not specified'
	genres: List[int]


class Error(Schema):
	message: str = None
