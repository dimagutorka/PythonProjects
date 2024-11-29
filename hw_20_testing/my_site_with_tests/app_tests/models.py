from django.db import models


class Tasks(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	due_date = models.DateField()