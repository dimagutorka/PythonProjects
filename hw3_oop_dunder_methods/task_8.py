class Price:

	def __init__(self, price: float):
		self.price = round(price, 2)

	def __add__(self, other):
		return self.price + other.price

	def __sub__(self, other):
		return self.price - other.price

	def __eq__(self, other):
		return self.price == other.price


# Instance creation
a = Price(200.5032545)
b = Price(100.25435453)
c = Price(200.5032545)


# Print the results of the arithmetic operations
print(a + b)  # -> 300.75
print(a - b)  # -> 100.25
print(a == b)  # -> False
print(a == c)  # -> True

