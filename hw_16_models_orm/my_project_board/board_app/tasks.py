from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now
from .models import Ad


@shared_task
def deactivate_old_ads():
    thirty_days_ago = now() - timedelta(days=30)
    Ad.objects.filter(is_active=True, created_at__lte=thirty_days_ago).update(is_active=False)
