class A:
	def __init__(self, a: any, b: any) -> None:
		"""Initializes the object with two attributes.

		Args:
			a (Any): The value for the first attribute.
			b (Any): The value for the second attribute.
		"""
		self.a = a
		self.b = b

	def inspect_func(self) -> None:
		"""Inspects the object and prints its type, methods, and attributes.

		This method retrieves:
		- The type of the object.
		- A list of all methods available for the object.
		- A dictionary of the object's attributes.
		- A dictionary of the types of all attributes.

		Prints:
			str: Formatted string containing the type, methods, attributes, and types of attributes.
		"""
		types_of_all_attr = {j: type(j) for i, j in vars(self).items()}

		print(f" Type - {type(self)} \n All methods of an object - {self.__dir__()} \n "
		      f"Attribute of the object -  {vars(self)} \n All attributes of the object - {types_of_all_attr}")


# Example usage
c = A(5, 6)
c.inspect_func()
