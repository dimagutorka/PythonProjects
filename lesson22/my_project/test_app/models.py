from django.db import models

from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections


connections.create_connection(hosts=['http://localhost:9201'])


class DataDocument(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


