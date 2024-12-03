from django.dispatch import receiver
from django.db.models.signals import post_save

from basic_site.models import Movies


@receiver(post_save, sender=Movies)
def add_poster_name(sender, created, instance, **kwargs):
	if created:
		instance.objects.update(poster=f'{instance.title}-{instance.country}-{instance.release_date}')