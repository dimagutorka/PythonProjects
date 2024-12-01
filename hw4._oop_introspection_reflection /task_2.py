def call_function(obj: object, method_name: str, *args: any) -> any:
	"""Calls a method of an object with the provided arguments.

		obj (object): The object containing the method to call.
		method_name (str): The name of the method to call.
		*args (any): The arguments to pass to the method.

	Returns:
		any: The result of the method call.
	"""
	method = getattr(obj, method_name)
	return method(*args)


class Example:

	def add(self, a: int, b: int) -> int:
		"""Adds two numbers together"""
		return a + b


# Example usage
example_obj = Example()
result = call_function(example_obj, 'add', 3, 5)
print(result)  # Output: 8
