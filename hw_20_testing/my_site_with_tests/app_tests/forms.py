from datetime import datetime, date

from django import forms
from app_tests.models import Tasks


class TaskForm(forms.ModelForm):
	title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(max_length=100, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
	due_date = forms.DateField()

	class Meta:
		model = Tasks
		fields = '__all__'

	def clean_due_date(self):
		due_date = self.cleaned_data['due_date']

		if not isinstance(due_date, date):
			raise forms.ValidationError("Invalid date format")

		if due_date < date.today():
			raise forms.ValidationError("Date must be in the future")

		return due_date
