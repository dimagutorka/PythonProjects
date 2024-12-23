from django import forms
from models import WatchLater, Movies


class AddToWatchLater(forms.ModelForm):
	class Meta:
		model = WatchLater
		fields = []


class MovieForm(forms.ModelForm):
	class Meta:
		model = Movies
		fields = ['title', 'release_date', 'country', 'genres', 'poster']
