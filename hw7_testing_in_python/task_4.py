import doctest


def is_even(n: int) -> bool:
	"""
	>>> is_even(2)
	True
	>>> is_even(1)
	False
	"""
	if n % 2 == 0:
		return True

	return False


def factorial(n: int) -> int:
	"""
	>>> factorial(1)
	1
	>>> factorial(0)
	Traceback (most recent call last):
		...
	ValueError: n should bigger than 0
	>>> factorial(5)
	120

	"""

	if n == 1:
		return 1
	elif n <= 0:
		raise ValueError('n should bigger than 0')
	return factorial(n - 1) * n


if __name__ == '__main__':
	doctest.testmod()