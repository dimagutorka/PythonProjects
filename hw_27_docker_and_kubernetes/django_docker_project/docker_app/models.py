from django.db import models


# models.py
class PostgresModel(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		db_table = 'postgres_model'
		managed = True  # Default database: PostgreSQL


class MySQLModel(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		db_table = 'mysql_model'
		managed = True  # Indicates Django should manage the table
