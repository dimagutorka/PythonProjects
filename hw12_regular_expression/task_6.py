import re

pattern = r'^(?!.*?[\s])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'


def password_validation(password):
	is_valid = re.fullmatch(pattern, password)

	if is_valid:
		return print('Your password is valid (:')
	return print('Your password is invalid ):')



#Negative test cases
password_validation('qqq')
password_validation('qqwweerr')
password_validation('qqwweerr1')
password_validation('qqwweerr1#')
password_validation(' qqwweerr1#')
password_validation('qqwweerr1# ')
password_validation('qqwwee rr1#')


#Positive test cases
password_validation('qqwweerr1%A')
password_validation('(^(%#*asfF2)%A')