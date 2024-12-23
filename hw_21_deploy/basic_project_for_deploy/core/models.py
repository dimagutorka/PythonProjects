from django.db import models
from django.contrib.auth.models import User
from movies.models import Movies


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


class FileCSV(models.Model):
	csv_filename = models.FileField(upload_to='movie_csv/', blank=True, null=True)
