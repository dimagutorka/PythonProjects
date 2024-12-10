from django import template
import datetime

register = template.Library()


@register.filter('my_cut')
def cut(value, arg):
	return value.replace(arg, '1')


@register.filter(is_safe=True)
def lower(value):
	return value.lower()


@register.simple_tag
def current_time(format_string):
	return datetime.datetime.now().strftime(format_string)
