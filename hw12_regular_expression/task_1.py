import re


pattern = r'^[a-zA-Z0-9]+([.]?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.(com|net|[a-zA-Z]{2,6})$'


def is_email_valid(email):
	if re.fullmatch(pattern, email):
		return print('Your email is valid!')
	return print('Your email is not valid!')


#Positive Checks
is_email_valid("user.name@domain.org")
is_email_valid("example@domain.com")

#Negative Checks
is_email_valid("example.@domain.com")
is_email_valid(".example@domain.com")
is_email_valid("user@-domain.com")


