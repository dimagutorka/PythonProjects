from django import forms
from models import FriendsList


# TODO-13: DELETE THE FORMS, I GUESS ITS REDUNDANT
class AddFriend(forms.ModelForm):
	class Meta:
		model = FriendsList
		fields = []


class AcceptFriend(forms.ModelForm):
	class Meta:
		model = FriendsList
		fields = []
