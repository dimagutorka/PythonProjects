from django.contrib import admin
from basic_site.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	date_hierarchy = 'birth_date'


