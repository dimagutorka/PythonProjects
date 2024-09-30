class BinaryNumber:

	def __init__(self, x):
		self.x = x

	def __and__(self, other):
		return self.x & other.x

	def __or__(self, other):
		return self.x | other.x

	def __xor__(self, other):
		return self.x ^ other.x

	def __invert__(self):
		return ~self.x


a = BinaryNumber(32)
b = BinaryNumber(16)

print(a & b)
print(a | b)
print(a ^ b)
print(~a)