def factorial(n):
	if n == 1:
		return 1
	return factorial(n-1) * n


def the_largest_common_divisor(number_1, number_2):
	the_largest_number = max(number_2, number_1)
	the_largest_divisor = 0

	for i in range(1, the_largest_number):
		if number_1 % i == 0 and number_2 % i == 0:
			if i > the_largest_divisor:
				the_largest_divisor = i

	return the_largest_divisor


