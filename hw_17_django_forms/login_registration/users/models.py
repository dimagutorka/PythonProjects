from django.db import models, connection
from django.contrib.auth.models import User


class UserManager(models.Manager):
	user_table_name = User._meta.db_table

	@staticmethod
	def fetch_users_with_status(is_active):
		query = f'SELECT id, username FROM {UserManager.user_table_name} WHERE is_active = %s'
		with connection.cursor() as cursor:
			cursor.execute(query, [is_active])
			result = cursor.fetchall()
		return result

	@staticmethod
	def id_gte(num):
		query = f'SELECT id, username from {UserManager.user_table_name} WHERE id >= %s'
		with connection.cursor() as cursor:
			cursor.execute(query, [num])
			result = cursor.fetchall()
		return result
		

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	location = models.CharField(max_length=50, blank=True)
	avatar = models.ImageField(upload_to="avatars/", blank=True, default="avatars/default.png")

	objects = UserManager()

	def __str__(self):
		return self.user.username


