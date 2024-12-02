from __future__ import absolute_import, unicode_literals
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')


app = Celery('my_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_tasks(self):
	print(f'request: {self.request!r}')