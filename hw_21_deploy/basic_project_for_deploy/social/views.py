from django.shortcuts import render


@login_required(login_url='/login_page/')
def user_profile_view(request, user_id):
	request_user_id = request.user
	user = User.objects.get(id=user_id)
	user_data = User.objects.select_related('profile').get(id=user_id)
	friend = FriendsList.objects.filter(user_id=request_user_id, friend_id=user_id).first()

	most_rated = user.rates.all().order_by('-rate')[:3]
	least_rated = user.rates.all().order_by('rate')[:3]

	friend_ids = FriendsList.objects.values_list('friend_id', flat=True).filter(user=request_user_id)

	if request.method == 'POST':

		if 'add_friend' in request.POST:
			user_fried_form = AddFriend(request.POST)
			if user_fried_form.is_valid():
				form = user_fried_form.save(commit=False)
				form.user = request_user_id
				form.friend = user
				form.save()

		if 'delete_friend' in request.POST:
			FriendsList.objects.get(friend_id=user_id).delete()

		return redirect('profile', user_id=user_id)

	context = {'user_data': user_data,
	           'most_rated': most_rated,
	           'least_rated': least_rated,
	           'user_id': user_id,
	           'friend_ids': friend_ids,
	           'friend': friend}

	return render(request, 'basic_site/user_profile.html', context)


@login_required(login_url='/login_page/')
def friends_list_view(request):
	request_user_id = request.user
	friend_ids = FriendsList.objects.values_list('user_id', flat=True).filter(friend_id=request_user_id,
	                                                                          is_friend=False)
	friend_requests = User.objects.filter(id__in=friend_ids)

	if request.method == 'POST':
		friend_id = request.POST.get('user_id', None)
		if "accept_friend" in request.POST:
			friend_entry = get_object_or_404(FriendsList, user_id=friend_id, friend_id=request_user_id)
			if not friend_entry.is_friend:
				friend_entry.is_friend = True
				friend_entry.save()
				messages.success(request, 'Friend accepted')
			else:
				messages.warning(request, 'You already accepted')

		elif "decline_friend" in request.POST:
			declined_friend = FriendsList.objects.filter(user_id=friend_id, friend_id=request_user_id)
			if declined_friend.exists():
				declined_friend.delete()
				messages.info(request, "Friend request declined.")
			else:
				messages.warning(request, 'You already declined')

		return redirect('friends_list')

	return render(request, 'basic_site/friends_list.html', {'friend_requests': friend_requests})
