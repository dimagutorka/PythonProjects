import multiprocessing
import concurrent.futures
from random import randint
import numpy as np
import time

big_array = [randint(1, 10) for _ in range(100)]
divided_arrays = []
summ_of_all_arrays = []


def data_array_division(array):
	a = np.array_split(array, 3)
	time.sleep(1)
	[divided_arrays.append(a[ind]) for ind, _ in enumerate(a)]


def sum_of_array(array):
	calc = sum(array)
	return calc


if __name__ == "__main__":
	data_array_division(big_array)

	with concurrent.futures.ProcessPoolExecutor() as executor:
		results = [executor.submit(sum_of_array, array) for array in divided_arrays]

		for f in concurrent.futures.as_completed(results):
			summ_of_all_arrays.append(f.result())

	print(sum(summ_of_all_arrays))








