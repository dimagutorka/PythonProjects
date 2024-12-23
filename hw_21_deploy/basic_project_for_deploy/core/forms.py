from django import forms
from core.models import Comments, Rate, FileCSV


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









