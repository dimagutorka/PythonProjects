from django.contrib import admin
from basic_site.models import UserProfile, Genres, Movies


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	date_hierarchy = 'birth_date'


admin.site.register(Movies)
admin.site.register(Genres)