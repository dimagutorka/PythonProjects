from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
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
	genres = models.ManyToManyField(Genres)

	def __str__(self):
		return self.title


class Comments(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

	def __str__(self):
		return self.content


class Tags(models.Model):
	name = models.CharField(max_length=100, unique=True)
	tag = models.ManyToManyField(Movies)

	def __str__(self):
		return self.name
