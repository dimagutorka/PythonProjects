from cryptography.fernet import Fernet
from django.db import models

key = Fernet.generate_key()


class EncryptedField(models.TextField):
	def __init__(self, *args, **kwargs):
		self.cipher = Fernet(key)
		kwargs['unique'] = True
		kwargs['blank'] = False
		super().__init__(*args, **kwargs)

	def get_prep_value(self, value):
		if value is not None:
			value = self.cipher.encrypt(value.encode()).decode()
		return super().get_prep_value(value)

	def from_db_value(self, value, expression, connection):
		if value is not None:
			value = self.cipher.decrypt(value.encode()).decode()
		return value


class SensitiveData(models.Model):
	name = models.CharField(max_length=100)
	sensitive_data = EncryptedField()


class Category(models.Model):
	name = models.CharField(max_length=100)


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
	available = models.BooleanField(default=True)
