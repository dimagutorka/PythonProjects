from django.contrib import admin
from basic_site.models import UserProfile, Genres, Movies


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	pass


admin.site.register(Movies)
admin.site.register(Genres)
