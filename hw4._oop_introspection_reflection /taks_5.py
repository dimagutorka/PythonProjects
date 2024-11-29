class MutableClass:

	def __init__(self, name: str, age: int) -> None:
		"""Initializes the instance with name and age attributes.

		Args:
			name (str): The name of the individual.
			age (int): The age of the individual.
		"""
		self.name = name
		self.age = age

	def set_attr_dynamically(self, **kwargs: dict) -> None:
		"""Sets attributes dynamically based on keyword arguments.

		Args:
			**kwargs: A variable length argument list of keyword arguments representing attribute names and their values.
		"""
		for k, v in kwargs.items():
			setattr(self, k, v)

	def del_attr_dynamically(self, *args: str) -> None:
		"""Deletes attributes dynamically based on provided names.

		Args:
			*args: A variable length argument list of attribute names to delete.
		"""
		for k in args:
			print(f"Deleting attribute: {k}")
			delattr(self, k)


# Example usage
person = MutableClass("Ivan", 25)
print(person.__dict__)  # Outputs: {'name': 'Ivan', 'age': 25}

person.set_attr_dynamically(last_name='Franko', money=400)
print(person.__dict__)  # Outputs: {'name': 'Ivan', 'age': 25, 'last_name': 'Franko', 'money': 400}

person.del_attr_dynamically('last_name', 'money')
print(person.__dict__)  # Outputs: {'name': 'Ivan', 'age': 25}
