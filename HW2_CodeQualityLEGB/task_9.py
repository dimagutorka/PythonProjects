def get_factorial(n):
	if n == 0:
		return 1
	return n * get_factorial(n-1)


def memoize(func):
	cache = {

	}

	def inner(n):
		if n in cache:
			print(f"Factorial {n} is already calculated and can be retrieved from cache")
			return cache[n]
		print(f"Factorial {n} is new and has to be calculated")
		result = func(n)
		cache[n] = result
		return result

	return inner


a = memoize(get_factorial)
print(a(4))
print(a(4))
