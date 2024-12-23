from django.db import models
from django.contrib.auth.models import User

class FriendsList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mainuser')
	friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
	is_friend = models.BooleanField(default=False)
	added_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('user', 'friend')