from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from basic_site.models import UserProfile, Movies


class UserProfileForm(forms.ModelForm):
	avatar = forms.ImageField(
		widget=forms.FileInput(attrs={'class': 'form-control-file'}),
		required=False)

	class Meta:
		model = UserProfile
		fields = ['avatar', 'bio', 'birth_date']


class UserForm(forms.ModelForm):
	class Meta:
		model = get_user_model() # == User
		fields = ['last_name', 'first_name', 'email']


class MovieForm(forms.ModelForm):
	class Meta:
		model = Movies
		fields = ['title', 'release_date', 'country', 'genres', 'rating']

