from django.contrib import admin
from core.models import UserProfile, Genres, Movies


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	pass


admin.site.register(Movies)
admin.site.register(Genres)
