from typing import List, Any


class A:
	"""A class to handle a list of numbers, providing methods to calculate sum and minimum."""

	def __init__(self, list_obj: List[float]) -> None:
		"""Initializes the class with a list of numbers.

		Args:
			list_obj (List[float]): The list of numbers to operate on.
		"""
		self.list_obj = list_obj
		self.list_sum = 0
		self.list_min = float('inf')  # Initialize to infinity for finding the minimum

	def __len__(self) -> int:
		"""Returns the length of the list."""
		return len(self.list_obj)

	def __iter__(self):
		"""Returns the iterator object (self) for the list."""
		self.n = 0
		return self

	def __next__(self) -> Any:
		"""Returns the next item from the list.

		Raises:
			StopIteration: When there are no more items to iterate.
		"""
		if 0 <= self.n < len(self.list_obj):
			result = self.list_obj[self.n]
			self.n += 1
			return result
		else:
			raise StopIteration

	def get_list_sum(self) -> float:
		"""Calculates the sum of the numbers in the list.

		Returns:
			float: The sum of the list elements.
		"""
		self.list_sum = sum(self.list_obj)  # Use built-in sum function
		return self.list_sum

	def get_list_min(self) -> float:
		"""Finds the minimum number in the list.

		Returns:
			float: The minimum value in the list.
		"""
		if not self.list_obj:
			raise ValueError("List is empty, cannot determine minimum.")

		self.list_min = min(self.list_obj)  # Use built-in min function
		return self.list_min


# Example usage
a = A([10, 52, 2, 3, 4, 5])

# Calculate the sum and minimum
sum_result = a.get_list_sum()
min_result = a.get_list_min()

print(f"Sum: {sum_result}")  # Output: Sum: 76
print(f"Minimum: {min_result}")  # Output: Minimum: 2
