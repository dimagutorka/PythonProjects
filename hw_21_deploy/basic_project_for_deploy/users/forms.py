from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from models import UserProfile


class UserProfileForm(forms.ModelForm):
	avatar = forms.ImageField(
		widget=forms.FileInput(attrs={'class': 'form-control-file'}),
		required=False)

	class Meta:
		model = UserProfile
		fields = ['avatar', 'bio', 'birth_date']


class UserForm(forms.ModelForm):
	class Meta:
		model = get_user_model()  # == User
		fields = ['last_name', 'first_name', 'email']


class RegistrationForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
	class Meta:
		model = get_user_model()
		fields = ['username', 'password']
