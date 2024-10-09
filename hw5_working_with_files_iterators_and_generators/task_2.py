import uuid
from typing import List

list_if_uuid: List[uuid.UUID] = []


def uuid_generator(number_of_uuid: int) -> None:
	"""
	Generates a specified number of UUIDs and appends them to the global list.

	Args:
		number_of_uuid (int): The number of UUIDs to generate.

	Returns:
		None: This function does not return a value. It modifies the global list `list_if_uuid`.
	"""
	for _ in range(number_of_uuid):
		list_if_uuid.append(uuid.uuid4())


# Generate 10 UUIDs
uuid_generator(10)

# Create an iterable object from the list of UUIDs
iterable_object = iter(list_if_uuid)

# Print the first three UUIDs from the iterable
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
