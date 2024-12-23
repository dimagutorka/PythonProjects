from django.shortcuts import render


@login_required(login_url='/login_page/')
def update_user_profile_view(request):
	if request.method == 'POST':

		form_user = UserForm(request.POST, instance=request.user)
		form_userprofile = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

		if form_user.is_valid() and form_userprofile.is_valid():
			form_user.save()
			form_userprofile.save()
			messages.success(request, 'Your profile has been updated')
			return redirect('home')

	else:
		form_user = UserForm(instance=request.user)
		form_userprofile = UserProfileForm(instance=request.user.profile)

	return render(request, 'basic_site/update_user.html', {
		'form_user': form_user,
		'form_userprofile': form_userprofile
	})


def login_view(request):
	form = LoginForm(request.POST or None)
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(request, username=username, password=password)

		if user is not None:
			request.session.flush()
			login(request, user)
			messages.success(request, f'Welcome back, {user.username}!')
			return redirect('home')
		else:
			messages.error(request, 'Invalid username or password.')
			return redirect('login_page')

	return render(request, 'basic_site/login_page.html', {"form": form})


def registration_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			request.session['username'] = user.username
			return redirect('home')
	else:
		form = RegistrationForm()
	return render(request, 'basic_site/registration_page.html', {'form': form})


@login_required(login_url='/login_page/')
def logout_view(request):
	logout(request)
	return redirect('home')
