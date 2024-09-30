class Vector:

	def __init__(self, point):
		self.point = point

	def __add__(self, other):
		return self.point + other.point

	def __sub__(self, other):
		return self.point - other.point

	def __mul__(self, other):
		return self.point * other.point

	def __lt__(self, other):
		return self.point < other.point

	def __eq__(self, other):
		return self.point == other.point

	# Get the length of the vector
	def get_vector_length(self):
		return f"the length of the Vector is {self.point}"


# Instance creation
a = Vector(1)
b = Vector(5)

# All arithmetic operations
add1 = a + b
sub1 = a - b
mul1 = a * b
lt1 = a < b
eq1 = a == b

# Print the results of the arithmetic operations
print(add1)
print(sub1)
print(mul1)
print(lt1)
print(eq1)

# Print the length of vector
print(a.get_vector_length())


