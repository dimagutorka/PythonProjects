import re
from django import forms
from django.contrib.auth.forms import UserCreationForm

from my_site.models import *


class RegisterForm(UserCreationForm):
	birth_date = forms.DateField(widget=forms.SelectDateWidget, required=False)
	address = forms.ChoiceField(widget=forms.Select, label="Select a product") 	#the name of the field is address just for testing a widget
	phone = forms.CharField(max_length=13)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['address'].widget.choices = [
			(product.name, f"{product.name} - ${product.price}") for product in Product.objects.all()
		]

	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		if phone and not re.match(r'^\+38\d{10}$', phone):
			raise forms.ValidationError('Your phone number is invalid.')
		return phone

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'birth_date', 'address', 'phone']


class TestForm(forms.ModelForm):
	phone = PhoneNumberFieldUA()
	birth_date = forms.DateField(widget=forms.SelectDateWidget)
	address = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = UserProfile
		fields = ['phone', 'birth_date', 'address']
