import concurrent.futures
import functools
import numpy as np


summa = []


def divide_into_small_factorials(array):
	sub_factors = []
	sub_factor = functools.reduce(lambda x, y: x * y, array)
	sub_factors.append(sub_factor)

	return sub_factors


def factorial():
	factor_result = functools.reduce(lambda x, y: x * y, summa)
	return factor_result


if __name__ == "__main__":
	with concurrent.futures.ProcessPoolExecutor() as executor:
		sections_to_divide = int(input('Enter the amount of sections to divide the process'))
		factor = int(input('Enter the factorial'))
		sub_arrays = np.array_split(list(range(1, factor + 1)), sections_to_divide)

		futures = [executor.submit(divide_into_small_factorials, array=array) for array in sub_arrays]

		for f in futures:
			summa.append(f.result()[0])

	print(factorial())