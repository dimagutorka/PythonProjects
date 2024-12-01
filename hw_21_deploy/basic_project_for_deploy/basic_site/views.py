from django.shortcuts import render, redirect
from basic_site.forms import UserProfileForm, UserForm
from django.contrib import messages


def update_user_profile(request):
	if request.method == 'POST':
		form_user = UserForm(request.POST, instance=request.user)
		form_userprofile = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

		if form_user.is_valid() and form_userprofile.is_valid():
			print(request.FILES.get('avatar'))

			form_user.save()
			form_userprofile.save()
			messages.success(request, 'Your profile has been updated')

			return redirect('home')

	else:

		form_user = UserForm(instance=request.user)
		form_userprofile = UserProfileForm(instance=request.user.userprofile)

	return render(request, 'basic_site/update_user.html', {'form_user': form_user,
	                                                       'form_userprofile': form_userprofile})


def home(request):
	return render(request, 'home.html')