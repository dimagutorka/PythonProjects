from django.contrib import admin, messages
from django.utils.translation.trans_real import ngettext

from my_site.models import *
import datetime


class UserProfileAdmin(admin.ModelAdmin):
	fields = ['user', 'phone', 'birth_date', 'address']
	list_filter = ['birth_date', 'user']
	actions = ['set_birthday', 'test']

	@admin.action(description='Set birthday for selected users')
	def set_birthday(self, request, queryset):
		queryset.update(birth_date=datetime.date.today())
		self.message_user(request, ngettext(
				'%d user has been successfully set birthday.',
				'%d users have been successfully set birthday.',
				queryset.count()) % queryset.count())

	@admin.action(description='TEST')
	def test(self, request, queryset):
		for query in queryset:
			if query.phone == '+384444444444':
				query.phone = '+385555555555'
				query.save()
				self.message_user(request, f'{query.user} phone number has been successfully changed')


class ProductInline(admin.StackedInline):
	model = Product
	extra = 5
	fields = ['name', 'price', 'available']


class CategoryAdmin(admin.ModelAdmin):
	inlines = [ProductInline]
	list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'available', 'category']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)




