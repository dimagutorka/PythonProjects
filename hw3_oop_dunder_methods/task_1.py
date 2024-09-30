class Fraction:
	"""
	 A class for presenting and working with fractions.
	 Supports addition, subtraction, multiplication and division of fractions.
	"""

	def __init__(self, number):
		self.number = number

	def __str__(self):
		return f"{self.number[0]} \n" + '-' * (len(str(max(self.number)))) + f"\n{self.number[1]}"

	# I use method 'as_integer_ratio' in subsequent class methods which converts float into fraction
	def __add__(self, other):
		result = self.number + other.number
		return Fraction(result.as_integer_ratio())

	def __sub__(self, other):
		result = self.number - other.number
		return Fraction(result.as_integer_ratio())

	def __mul__(self, other):
		result = self.number * other.number
		return Fraction(result.as_integer_ratio())

	def __truediv__(self, other):
		result = self.number / other.number
		return Fraction(result.as_integer_ratio())


# Instance creation
a = Fraction(0.1)
b = Fraction(0.5)

# Print the results of the arithmetic operations
print(a + b)
print(a - b)
print(a * b)
print(a / b)
