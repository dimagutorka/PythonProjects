import re  # Regular expressions module for pattern matching

# Regular expression pattern for password validation
pattern = r'^(?!.*?[\s])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'


def password_validation(password: str) -> None:
	"""
	Validates a password based on the specified criteria:
	- No spaces allowed.
	- At least one lowercase letter.
	- At least one uppercase letter.
	- At least one digit.
	- At least one special character from the set #?!@$%^&*-.
	- Minimum length of 8 characters.

	Parameters:
	password (str): The password to be validated.

	Returns:
	None: Prints whether the password is valid or invalid.
	"""
	# Check if the password matches the pattern
	is_valid = re.fullmatch(pattern, password)

	if is_valid:
		return print('Your password is valid (:')
	return print('Your password is invalid ):')


# Negative test cases: Expected to print "Your password is invalid ):"
password_validation('qqq')  # Too short, no uppercase, digit, or special character
password_validation('qqwweerr')  # No uppercase, digit, or special character
password_validation('qqwweerr1')  # No uppercase or special character
password_validation('qqwweerr1#')  # No uppercase character
password_validation(' qqwweerr1#')  # Has a leading space
password_validation('qqwweerr1# ')  # Has a trailing space
password_validation('qqwwee rr1#')  # Contains a space inside

# Positive test cases: Expected to print "Your password is valid (:"
password_validation('qqwweerr1%A')  # Meets all criteria
password_validation('(^(%#*asfF2)%A')  # Meets all criteria
