from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def price_validator(value):
	if value >= 0:
		return value
	raise ValidationError("The price cannot be less than or equal to zero.")


class User(AbstractUser):
	address = models.CharField(max_length=120)
	phone = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.username


class Category(models.Model):
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	is_active = models.BooleanField(default=True)

	@staticmethod
	def active_posts():
		active_posts = Category.objects.filter(is_active=True)
		return print(f"You have {active_posts.count()} active posts")

	def __str__(self):
		return self.name


class Ad(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	price = models.IntegerField(null=True, blank=True, validators=[price_validator])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def print_short_description(self):
		print(f"Here's the short description of {self.description[:100]}")

	def deactivate_add(self):
		pass

	def __str__(self):
		return self.title


class Comment(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	@staticmethod
	def amount_of_comments(ad_id):
		comments = Comment.objects.filter(ad=Ad.objects.get(title=ad_id))
		print(f'The ad has {comments.count()} comments')

	def __str__(self):
		return f'Comment was added by {self.user} for {self.ad}'
