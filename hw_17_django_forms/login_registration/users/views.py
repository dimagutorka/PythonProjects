from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import AuthenticationForm
from users.forms import RegistrationForm, UpdateUserForm, UpdateUserProfileForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required


def registration_view(request):
	if request.method == 'GET':
		form = RegistrationForm()
		return render(request, 'users/registration_page.html', {'form': form})

	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful. You are now logged in!")
			return redirect('home')

		else:
			return render(request, 'users/registration_page.html', {'form': form})


def login_view(request):
	form = AuthenticationForm()

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is None:
			context = {'error': 'invalid username or password', 'form': form}
			return render(request, 'users/login_page.html', context)

		login(request, user)
		return redirect('home')

	return render(request, 'users/login_page.html', {'form': form})


def logout_view(request):
	logout(request)
	return redirect('home')


@login_required(login_url='no_account')
def update_user_profile(request):
	if request.method == 'POST':

		user_form = UpdateUserForm(request.POST, instance=request.user)
		profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()

			messages.success(request, 'Your profile was successfully updated!')
			return redirect('profile')

	else:
		user_form = UpdateUserForm(instance=request.user)
		profile_form = UpdateUserProfileForm(instance=request.user.userprofile)

	return render(request, 'users/update_user.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required(login_url='no_account')
def change_password_view(request):
	if request.method == 'POST':
		form = CustomPasswordChangeForm(user=request.user, data=request.POST)
		CustomPasswordChangeForm(user=request.user)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, f'Your password was successfully updated!')

			return redirect(reverse('profile'))
	else:
		form = CustomPasswordChangeForm(user=request.user)
	return render(request, 'users/change_password.html', {'form': form})


@login_required(login_url='no_account')
def user_profile(request):
	return render(request, 'users/user_profile.html')


def home(request):
	return render(request, 'users/home.html')


def no_account(request):
	return render(request, 'users/no_account.html')

