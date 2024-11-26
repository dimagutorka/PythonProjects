from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	location = models.CharField(max_length=50, blank=True)
	avatar = models.ImageField(upload_to="avatars/", blank=True, default="avatars/default.png")

	def __str__(self):
		return self.user.username


