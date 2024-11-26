import re

class User:
    """A class to represent a user with first name, last name, and email address."""

    regex: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """Initializes the User with first name, last name, and email.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email address of the user.
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self) -> str:
        """First name property."""
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Sets the first name of the user.

        Args:
            value (str): The first name to set.
        """
        self.__first_name = value

    @property
    def last_name(self) -> str:
        """Last name property."""
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Sets the last name of the user.

        Args:
            value (str): The last name to set.
        """
        self.__last_name = value

    @property
    def email(self) -> str:
        """Email property."""
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """Sets the email address of the user.

        Args:
            value (str): The email address to set.
        """
        self.__email = value

    def email_validator(self) -> None:
        """Validates the user's email address against the defined regex pattern.

        Prints whether the email is valid or invalid.
        """
        if re.fullmatch(User.regex, self.__email):
            print("Valid Email")
        else:
            print("Invalid Email")

# Example usage
a = User("Ivan", "Franko", "Ivan_Franko@gmail.com")

# Print initial values
print(a.first_name)
print(a.last_name)
print(a.email)

# Change values
a.first_name = "Taras"
a.last_name = "Bulba"
a.email = "Taras_Bulba@gmail.com"

# Print updated values
print(" \nValues after changes: \n")
print(a.first_name)
print(a.last_name)
print(a.email)

# Validate email
a.email_validator()
