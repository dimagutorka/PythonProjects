from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from users.models import UserProfile


class RegistrationForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ['username', 'password1', 'password2', 'email']

	def clean_password2(self):
		cd = self.cleaned_data
		if cd.get('password1') != cd.get('password2'):
			raise forms.ValidationError('Passwords must match')
		return cd['password2']  # Return the valid password2 after confirmation

	def clean_email(self):
		if get_user_model().objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError('User with this email already exists')
		return self.cleaned_data['email']

	def clean_username(self):
		if get_user_model().objects.filter(username=self.cleaned_data['username']).exists():
			raise forms.ValidationError('User with this username already exists')
		return self.cleaned_data['username']


class UpdateUserForm(forms.ModelForm):
	username = forms.CharField(max_length=100,
	                           required=True,
	                           widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(required=True,
	                         widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = get_user_model()
		fields = ['username', 'email']


class LogInForm(UpdateUserForm, AuthenticationForm):
	class Meta:
		model = get_user_model()
		fields = ['username', 'email']


class UpdateUserProfileForm(forms.ModelForm):
	avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
	bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)
	birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
	location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

	class Meta:
		model = UserProfile
		fields = ['avatar', 'bio', 'location', 'birth_date']

	def clean_avatar(self):
		avatar = self.cleaned_data.get('avatar')
		if avatar:
			mb = 5
			max_size = (1024 * 1024) * mb
			if avatar.size > max_size:
				raise forms.ValidationError(f'Image\' size cannot be more than {mb} mb')

		return avatar


class CustomPasswordChangeForm(PasswordChangeForm):
	class Meta:
		model = get_user_model()
		fields = ['old_password', 'new_password1', 'new_password2']

	def clean(self):
		# Call the parent class's clean method to preserve default validations
		cleaned_data = super().clean()

		# Get the old and new passwords from the cleaned data
		old_password = cleaned_data.get('old_password')
		new_password = cleaned_data.get('new_password1')

		if old_password and new_password and old_password == new_password:
			raise forms.ValidationError("The new password cannot be the same as the old password.")
		return cleaned_data