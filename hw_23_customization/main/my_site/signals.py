from django.dispatch import receiver
from django.db.models.signals import post_save
from my_site.models import UserProfile
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
	else:
		instance.userprofile.save()