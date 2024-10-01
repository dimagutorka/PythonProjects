def analyze_inheritance(cls: type) -> None:
	"""Analyzes a class for inherited methods from its base classes.

	Args:
		cls (type): The class to analyze.

	Prints:
		- The name of the class.
		- A list of inherited methods from base classes.
	"""
	# Get a set of methods defined in the class
	own_methods = {method for method in dir(cls) if callable(getattr(cls, method))}

	# Get a set of methods from the base classes
	inherited_methods = set()
	for base in cls.__bases__:
		inherited_methods.update(
			{method for method in dir(base) if callable(getattr(base, method))})

	# Find methods that are inherited
	inherited_from_bases = own_methods.intersection(inherited_methods)

	# Print class name and inherited methods
	print(f"Class: {cls.__name__}")
	print("Inherited methods from base classes:")
	for method in inherited_from_bases:
		print(f" - {method}")


class Base:
	"""A base class with a method that can be inherited."""

	def base_method(self) -> None:
		"""A method in the base class."""
		pass


class Derived(Base):
	"""A derived class that inherits from Base."""

	def derived_method(self) -> None:
		"""A method in the derived class."""
		pass


# Example usage
analyze_inheritance(Derived)
