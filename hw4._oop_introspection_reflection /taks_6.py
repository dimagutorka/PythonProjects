class Proxy:
	"""A Proxy class that forwards method calls to an underlying object and logs the calls.

	Attributes:
		_obj (object): The object to proxy.

	Methods:
		__getattr__(method_name: str): Intercepts method calls and logs the call details.
	"""

	def __init__(self, obj: object) -> None:
		"""Initializes the Proxy with the provided object.

		Args:
			obj (object): The object to proxy.
		"""
		self._obj = obj

	def __getattr__(self, method_name: str) -> callable:
		"""Intercepts method calls to the proxied object.

		Args:
			method_name (str): The name of the method to call.

		Returns:
			callable: A callable that logs the method call and forwards it to the actual method.
		"""
		original_method = getattr(self._obj, method_name)

		def wrapped(*args: any, **kwargs: any) -> any:
			print(f"Calling method: {method_name} with arguments: {args} and keyword arguments: {kwargs}")
			return original_method(*args, **kwargs)

		return wrapped


class Example:
	"""A simple example class to demonstrate method calling.

	Methods:
		add(a: int, b: int) -> int: Returns the sum of two integers.
		subtract(a: int, b: int) -> int: Returns the difference between two integers.
	"""

	def add(self, a: int, b: int) -> int:
		"""Adds two numbers together.

		Args:
			a (int): The first number to add.
			b (int): The second number to add.

		Returns:
			int: The sum of a and b.
		"""
		return a + b

	def subtract(self, a: int, b: int) -> int:
		"""Subtracts the second number from the first.

		Args:
			a (int): The number from which to subtract.
			b (int): The number to subtract.

		Returns:
			int: The difference of a and b.
		"""
		return a - b


# Example usage
example_obj = Example()
proxy = Proxy(example_obj)

result_add = proxy.add(5, 3)
result_subtract = proxy.subtract(10, 4)

print(result_add)  # Output: 8
print(result_subtract)  # Output: 6
