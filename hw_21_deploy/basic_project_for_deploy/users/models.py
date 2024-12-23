from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
	age = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return self.user.username
