class ProductWithGetSet:
	"""A class representing a product using getter and setter methods for price."""

	def __init__(self, name: str, price: float) -> None:
		"""Initializes the product with a name and price.

		Args:
			name (str): The name of the product.
			price (float): The price of the product.
		"""
		self.__name = name
		self.__price = price

	def get_price(self) -> float:
		"""Returns the price of the product.

		Returns:
			float: The current price of the product.
		"""
		return self.__price

	def set_price(self, value: float) -> None:
		"""Sets the price of the product if the value is non-negative.

		Args:
			value (float): The new price for the product.

		Raises:
			ValueError: If the price is negative.
		"""
		if value < 0:
			raise ValueError("Price cannot be negative.")
		self.__price = value


# Example usage of ProductWithGetSet
a_product = ProductWithGetSet("iPhone", 100)

print("Product price (get/set):", a_product.get_price())  # Output: 100
a_product.set_price(500)
print("Updated product price:", a_product.get_price())  # Output: 500
try:
	a_product.set_price(-200)  # This will raise ValueError
except ValueError as e:
	print(e)


class ProductWithProperty:
	"""A class representing a product using property decorators for price."""

	def __init__(self, name: str, price: float) -> None:
		"""Initializes the product with a name and price.

		Args:
			name (str): The name of the product.
			price (float): The price of the product.
		"""
		self.__name = name
		self.__price = price

	@property
	def price(self) -> float:
		"""Gets the price of the product.

		Returns:
			float: The current price of the product.
		"""
		return self.__price

	@price.setter
	def price(self, value: float) -> None:
		"""Sets the price of the product if the value is non-negative.

		Args:
			value (float): The new price for the product.

		Raises:
			ValueError: If the price is negative.
		"""
		if value < 0:
			raise ValueError("Price cannot be negative.")
		self.__price = value


# Example usage of ProductWithProperty
b_product = ProductWithProperty("iPhone", 50.50)

print("Initial product price (property):", b_product.price)  # Output: 50.50
b_product.price = 10.25
print("Updated product price (property):", b_product.price)  # Output: 10.25
try:
	b_product.price = -100  # This will raise ValueError
except ValueError as e:
	print(e)


class ProductPriceDescriptor:
	"""Descriptor for managing product price."""

	def __init__(self):
		self._price = 0.0

	def __get__(self, instance, owner):
		return self._price

	def __set__(self, instance, value):
		if value < 0:
			raise ValueError("Price cannot be negative.")
		self._price = value


class ProductWithDescriptor:
	"""A class representing a product using a descriptor for price."""

	price = ProductPriceDescriptor()  # Using the descriptor

	def __init__(self, name: str, price: float) -> None:
		"""Initializes the product with a name and price.

		Args:
			name (str): The name of the product.
			price (float): The price of the product.
		"""
		self.__name = name
		self.price = price  # Use the descriptor's setter


# Example usage of ProductWithDescriptor
descriptor_product = ProductWithDescriptor("iPhone", 100.0)
print("Product price (descriptor):", descriptor_product.price)  # Output: 100.0
descriptor_product.price = 200.0
print("Updated product price (descriptor):", descriptor_product.price)  # Output: 200.0
try:
	descriptor_product.price = -50  # This will raise ValueError
except ValueError as e:
	print(e)
