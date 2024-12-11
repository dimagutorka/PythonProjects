from __future__ import absolute_import, unicode_literals

import os
from django.conf import settings
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basic_project_for_deploy.settings")

app = Celery('basic_project_for_deploy')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
	print(f'Request: {self.request!r}')
