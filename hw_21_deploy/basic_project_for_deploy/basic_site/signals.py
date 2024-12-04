from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.db.models import Avg
from basic_site.models import Movies, Rate


@receiver(post_delete, sender=Rate)
@receiver(post_save, sender=Rate)
def calculate_avg_rate_after_creation(sender, instance, **kwargs):
	movie = instance.movie
	avg_rate = movie.rates.all().aggregate(Avg('rate'))['rate__avg']
	movie.average_rate = avg_rate if avg_rate is not None else 0
	movie.save()



