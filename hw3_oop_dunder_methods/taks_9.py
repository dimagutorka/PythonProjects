class ProductWithGetSet:

	def __init__(self, name: str, price: float):
		self.__name = name
		self.__price = price

	def get_price(self):
		return self.__price

	def set_price(self, value):
		if value < 0:
			raise ValueError
		self.__price = value


a_product = ProductWithGetSet("iPhone", 100)

print(a_product.get_price())  # get and display a price -> 100
a_product.set_price(500)  # set a new price
print(a_product.get_price())  # get and disp lay the new price -> 500
a_product.set_price(-200)  # set a negative price



class ProductWithProperty:

	def __init__(self, name: str, price: float):
		self.__name = name
		self.__price = price

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, value):
		if value < 0:
			raise ValueError
		else:
			self.__price = value


b_product = ProductWithProperty("iPhone", 50.50)

print(b_product.price)  # display the price -> 50.5
b_product.price = 10.25  # set a new price
print(b_product.price)  # display the price -> 10.25
b_product.price = -100  # set a negative price


class ProductWithDescriptor:
	pass


#https://www.youtube.com/watch?v=ACqsYPbgePk&ab_channel=selfedu