import re


class User:

	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

	def __init__(self, first_name, last_name, email):
		self.__first_name = first_name
		self.__last_name = last_name
		self.__email = email

	@property
	def first_name(self):
		return self.__first_name

	@first_name.setter
	def first_name(self, value):
		self.__first_name = value

	@property
	def last_name(self):
		return self.__last_name

	@last_name.setter
	def last_name(self, value):
		self.__last_name = value

	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, value):
		self.__email = value

	def email_validator(self):
		# pass the regular expression
		# and the string into the fullmatch() method
		if re.fullmatch(User.regex, self.__email):
			print("Valid Email")

		else:
			print("Invalid Email")


a = User("Ivan", "Franko", "Ivan_Franko@gmail.com")

print(a.first_name)
print(a.last_name)
print(a.email)

# Set new value to our object
a.first_name = "Taras"
a.last_name = "Bulba"
a.email = "Taras_Bulba@gmail.com"

print(" \nValues after changes: \n")
print(a.first_name)
print(a.last_name)
print(a.email)

a.email_validator()  # check weather or email is valid or not

