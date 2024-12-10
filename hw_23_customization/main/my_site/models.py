import re

from cryptography.fernet import Fernet
from django.contrib.auth.models import User
from django.db import models, connection
from django.core.exceptions import ValidationError


class ProductManager(models.Manager):
	def product_counts(self):
		with connection.cursor() as cursor:
			cursor.execute("SELECT name ,COUNT(*) FROM my_site_product ORDER BY name ")
			rows = cursor.fetchall()
			return rows

	def available_products(self, is_available):
		with connection.cursor() as cursor:
			cursor.execute("SELECT name, available FROM my_site_product WHERE available = %s ", [is_available])
			rows = cursor.fetchall()
			return rows


class EncryptedField(models.TextField):
	key = Fernet.generate_key()

	def __init__(self, *args, **kwargs):
		self.cipher = Fernet(self.key)
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


class PhoneNumberFieldUA(models.CharField):

	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 13
		super().__init__(*args, **kwargs)

	def to_python(self, value):
		if value is None:
			return None
		return value

	def get_prep_value(self, value):
		if value is None:
			return ''
		return value


	@staticmethod
	def validate_ua_number(value):
		if not re.match(r'^\+38\d{10}$', value):
			raise ValidationError('Phone number must be in UA format +380*********')
		return value

	def formfield(self, **kwargs):
		from django import forms
		defaults = {
			'form_class': forms.CharField,
			'max_length': self.max_length,
			'validators': [self.validate_ua_number]
		}

		defaults.update(kwargs)
		return super().formfield(**defaults)


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = PhoneNumberFieldUA(validators=[PhoneNumberFieldUA.validate_ua_number])
	birth_date = models.DateField(null=True, blank=True)
	address = models.TextField(blank=True)


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

	objects = ProductManager()
