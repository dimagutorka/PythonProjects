import re


pattern = r'^([0-9]{10}|[(][0-9]{3}[)][\s][0-9]{3}-[0-9]{4}|[0-9]{3}[.][0-9]{3}[.][0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})'


def phone_number_filter(phone_number):
	a = re.fullmatch(pattern, phone_number)
	print(a)


# POSITIVE SCENARIOS
phone_number_filter('(123) 456-7890')
phone_number_filter('123-456-7890')
phone_number_filter('123.456.7890')
phone_number_filter('1234567890')


print('-' * 25)


# NEGATIVE SCENARIOS
phone_number_filter('(123  456-7890')
phone_number_filter('(123 456-7890')
phone_number_filter('(123)) 456-7890')
phone_number_filter('(123)) 456 7890')

phone_number_filter('123--456-7890')
phone_number_filter('123.456..7890')
phone_number_filter('123456.7890')

phone_number_filter(' 1234567890 ')
phone_number_filter('123 4567890')
phone_number_filter(' 1234567890')








# pattern = r'^([\d]{10}|([0-9]{3}[)]?[\s]?[-]?[.]?       [\d]+)'

