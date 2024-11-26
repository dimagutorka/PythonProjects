import re

# Regex pattern to validate an email address format
pattern: str = r'^[a-zA-Z0-9]+([.]?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.(com|net|[a-zA-Z]{2,6})$'


def is_email_valid(email: str) -> None:
	"""
	Validates an email address using a regular expression pattern.

	Parameters:
	email (str): The email address to be validated.

	Returns:
	None: Prints whether the email is valid or not.
	"""
	# Check if the email matches the pattern exactly
	if re.fullmatch(pattern, email):
		print('Your email is valid!')
	else:
		print('Your email is not valid!')


# Positive Checks (Expected to print "Your email is valid!")
is_email_valid("user.name@domain.org")  # Valid: Proper format with a period in the local part
is_email_valid("example@domain.com")  # Valid: Simple, standard format

# Negative Checks (Expected to print "Your email is not valid!")
is_email_valid("example.@domain.com")  # Invalid: Ends with a period in the local part
is_email_valid(".example@domain.com")  # Invalid: Starts with a period in the local part
is_email_valid("user@-domain.com")  # Invalid: Domain cannot start with a hyphen
