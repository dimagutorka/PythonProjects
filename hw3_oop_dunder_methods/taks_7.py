class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		if self.x:
			return self.x + self.x
		return self.y + self.y

	def __sub__(self, other):
		if self.x:
			return self.x - self.x
		return self.y - self.y

	def __mul__(self, other):
		if self.x:
			return self.x * self.x
		return self.y * self.y

	def __eq__(self, other):
		if self.x:
			return self.x == self.x
		return self.y == self.y


vector_a = Vector(10, 5)
vector_b = Vector(20, 10)

print(vector_a.x + vector_b.x)
print(vector_a.x - vector_b.x)
print(vector_a.x * vector_b.x)
print(vector_a.x == vector_b.x) #Comparition of the lenghts of two vectors

print("\t")

print(vector_a.y + vector_b.y)
print(vector_a.y - vector_b.y)
print(vector_a.y * vector_b.y)
print(vector_a.y == vector_b.y) #Comparition of the lenghts of two vectors







