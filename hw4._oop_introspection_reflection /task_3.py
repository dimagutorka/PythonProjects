import inspect
import math


def analyze_module(module: object) -> None:
	"""Analyzes a module to print its functions and the signature of a specific function.

	Args:
		module (object): The module to analyze, expected to be a Python module (e.g., math).

	Prints:
		- All callable functions in the specified module.
		- The signature of the factorial function in the module.
	"""
	print("All functions of the module:")
	for name, member in inspect.getmembers(module):
		if callable(member):
			print(name)  # Print the name of the callable function

	print(22 * "_")
	print(f"All signature of the module {inspect.signature(module.factorial)}")
	print(22 * "_")


# Example usage
analyze_module(math)
