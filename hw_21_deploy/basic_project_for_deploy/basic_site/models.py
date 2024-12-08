from django.db import models
from django.contrib.auth.models import User


class MovieManager(models.Manager):
	def num_comments(self, num_comments):
		return self.raw(""
		                "SELECT basic_site_movies.title, COUNT(*) "
		                "FROM basic_site_movies INNER JOIN basic_site_comments "
		                "ON basic_site_movies.id = basic_site_comments.movie_id "
		                "GROUP BY basic_site_movies.title "
		                "HAVING COUNT(*) > %s;",
		                [num_comments])

	def num_movies(self):
		return self.raw('SELECT COUNT(*) FROM basic_site_movies')


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=False, blank=True)
	avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

	def __str__(self):
		return self.user.username


class Genres(models.Model):
	name = models.CharField(max_length=20, unique=True, db_index=True)

	def __str__(self):
		return self.name


class Movies(models.Model):
	title = models.CharField(max_length=100, unique=True, db_index=True)
	overview = models.TextField(max_length=500, blank=True) #NEW
	release_date = models.DateField(null=True, blank=True)
	country = models.CharField(max_length=100)
	genres = models.ManyToManyField(Genres, related_name='movies')
	poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True,
	                           default='movie_posters/default-poster.jpg')
	adult = models.BooleanField(default=False) #NEW
	average_rating = models.FloatField(default=0.0)

	objects = MovieManager()

	def __str__(self):
		return self.title

	class Meta:
		indexes = [
			models.Index(fields=['title', 'release_date', 'country', 'poster', 'average_rating']),
		]


class Comments(models.Model):
	content = models.TextField(db_index=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
	movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return self.content


class Tags(models.Model):
	name = models.CharField(max_length=100, unique=True)
	tag = models.ManyToManyField(Movies, related_name='tags')

	def __str__(self):
		return self.name


class Rate(models.Model):
	rate = models.PositiveIntegerField(db_index=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
	movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='rates')

	class Meta:
		unique_together = ('user', 'movie')



