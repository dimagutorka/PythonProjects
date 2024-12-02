from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_task(subject, message, from_email, recipient_list):
	send_mail(subject, message, from_email, recipient_list, fail_silently=False)


@shared_task
def test_task():
	return "Test task executed"
