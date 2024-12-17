from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from basic_site.models import UserProfile, Movies, Comments, Rate, FileCSV, WatchLater


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


class MovieForm(forms.ModelForm):
	class Meta:
		model = Movies
		fields = ['title', 'release_date', 'country', 'genres', 'poster']


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['content']


class RateForm(forms.ModelForm):
	RATE_CHOICES = [(x, str(x)) for x in range(0, 11)]

	rate = forms.TypedChoiceField(
		choices=RATE_CHOICES,
		coerce=int,
		widget=forms.RadioSelect,
	)

	class Meta:
		model = Rate
		fields = ['rate']


class CSVFileForm(forms.ModelForm):
	class Meta:
		model = FileCSV
		fields = ['csv_filename']


class RegistrationForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
	class Meta:
		model = get_user_model()
		fields = ['username', 'password']


class AddToWatchLater(forms.ModelForm):
	class Meta:
		model = WatchLater
		fields = []