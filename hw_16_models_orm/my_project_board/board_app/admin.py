from django.contrib import admin
from board_app.models import Category, Ad, Comment, User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin


class CategoryAdmin(admin.ModelAdmin):
	list_filter = ['name']


class AdAdmin(admin.ModelAdmin):
	list_filter = ['is_active', 'category__name']
	fieldsets = [
		("Top", {"fields": ["title", 'is_active']}),
		("Date information", {"fields": ["description", "price"]}),
		("User", {"fields": ['user']}),
		("Category", {"fields": ['category']}),

	]


class UserAdmin(admin.ModelAdmin):
	fieldsets = DefaultUserAdmin.fieldsets + (('Additional Info', {'fields': ('address', 'phone'), }),)

	add_fieldsets = (
		(None, {
			"classes": ("wide",),
			"fields": ("username", "usable_password", "password1", "password2", 'address', 'phone'),
		}),
	)


class CommentAdmin(admin.ModelAdmin):
	fieldsets = (

			('Top', {'fields': ('content',), }),
			('Bottom', {'fields': ('ad', 'user',), })

	)

	add_fieldsets = (
		(None, {
			"classes": ("wide",),
			"fields": ('content', 'ad', 'user'),
		}),
	)


admin.site.register(User, UserAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
