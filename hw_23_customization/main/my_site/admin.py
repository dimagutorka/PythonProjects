from django.contrib import admin
from my_site.models import *



class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name",)
	search_fields = ("name",)
	list_filter = ("name",)


class ProductAdmin(admin.ModelAdmin):
	list_display = ("name", "price", "category", "available",)
	search_fields = ("price",)
	list_filter = ("available",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)