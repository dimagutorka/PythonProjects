from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=False, blank=True)
	avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

	def __str__(self):
		return self.user.username


class Genres(models.Model):
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name


class Movies(models.Model):
	title = models.CharField(max_length=100, unique=True)
	release_date = models.DateField(null=True, blank=True)
	country = models.CharField(max_length=100)
	genres = models.ManyToManyField(Genres, related_name='movies')
	rating = models.IntegerField(default=0)
	poster = models.TextField(blank=True)

	def __str__(self):
		return self.title


class Comments(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
	movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return self.content


class Tags(models.Model):
	name = models.CharField(max_length=100, unique=True)
	tag = models.ManyToManyField(Movies, related_name='tags')

	def __str__(self):
		return self.name
