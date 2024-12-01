from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from board_app.models import Category, Ad, Comment, User


@receiver(pre_save, sender=Comment)
def my_handler(sender, instance, **kwargs):
	print('Comment was saved')
	if instance.content == 'Bad':
		print(instance.content)
	else:
		print('Nothing')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_receiver(sender, instance, created, **kwargs):
	if created:
		print(f'User {instance.username} was created')
	else:
		print(f'User {instance.username} was updated')
