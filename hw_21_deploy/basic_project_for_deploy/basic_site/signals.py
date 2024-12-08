from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.db.models import Avg
from basic_site.models import Movies, Rate, Genres
from django.core.cache import cache


@receiver(post_delete, sender=Rate)
@receiver(post_save, sender=Rate)
def calculate_avg_rate_after_creation(sender, instance, **kwargs):
	movie = instance.movie
	avg_rate = movie.rates.aggregate(Avg('rate'))['rate__avg']
	movie.average_rating = avg_rate if avg_rate is not None else 0
	movie.save()


@receiver(post_delete, sender=Movies)
@receiver(post_save, sender=Movies)
def cache_refresh(sender, instance, **kwargs):
	print("Refreshing genres cache...")
	all_genres = Genres.objects.prefetch_related('movies')
	cache.set('genres', all_genres,  timeout=3600)
	print("Refreshing genres cache is done!")
