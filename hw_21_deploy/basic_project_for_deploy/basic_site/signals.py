from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.db.models import Avg
from basic_project_for_deploy import settings
from basic_site.models import Movies, Rate, Genres, Comments, UserProfile
from django.core.cache import cache
from django.core.mail import send_mail
from django.contrib.auth.models import User


@receiver(post_delete, sender=Rate)
@receiver(post_save, sender=Rate)
def calculate_avg_rate_after_creation(instance, **kwargs):
    movie = instance.movie
    avg_rate = movie.rates.aggregate(Avg("rate"))["rate__avg"]
    movie.average_rating = avg_rate if avg_rate is not None else 0
    movie.save()


# @receiver(post_delete, sender=Movies)
# @receiver(post_save, sender=Movies)
# def cache_refresh(**kwargs):
#     # CLEAR CACHE ????
#     print("Refreshing movies cache...")
#     all_genres = Genres.objects.prefetch_related("movies")
#     cache.set("genres", all_genres, timeout=3600)
#     print("Refreshing movies cache is done!")


@receiver(post_save, sender=User)
def user_registration_email(sender, instance, created, **kwargs):

    subject = f"Hello from our site!"
    recipient_list = ["dhutorka@gmail.com", "dgutorka@gmail.com"]

    if created:
        message = f"Hello {instance.username}! Thanks for registering!"
        send_mail(
            subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
        )


# Доделать указывая на то кто оставил коммент, под каким фильмом
@receiver(post_save, sender=Comments)
def user_registration_email(created, instance, **kwargs):
    subject = f"Someone has left the comment !"
    message = f"User has left the comment !"
    recipient_list = ["dhutorka@gmail.com", "dgutorka@gmail.com"]

    if created:
        send_mail(
            subject,
            message=message,
            from_email=settings.EMAIL_HOST,
            recipient_list=recipient_list,
        )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
