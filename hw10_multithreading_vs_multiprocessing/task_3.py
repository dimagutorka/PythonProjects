import concurrent.futures
from random import randint
import numpy as np
import time
from typing import List

# Generate a large array of random integers
big_array: List[int] = [randint(1, 10) for _ in range(100)]
divided_arrays: List[np.ndarray] = []  # List to hold divided sub-arrays
summ_of_all_arrays: List[int] = []  # List to hold the sum of each sub-array


def data_array_division(array: List[int]) -> None:
    """
    Splits the input array into three parts and adds each sub-array to divided_arrays.

    Args:
        array (List[int]): The array to split.

    This function splits the array into three equal parts using np.array_split,
    simulates a delay, and then appends each part to the divided_arrays list.
    """
    # Split array into 3 parts
    a = np.array_split(array, 3)
    time.sleep(1)  # Simulate a delay
    # Append each sub-array to divided_arrays
    [divided_arrays.append(a[ind]) for ind, _ in enumerate(a)]


def sum_of_array(array: np.ndarray) -> int:
    """
    Calculates the sum of the elements in an array.

    Args:
        array (np.ndarray): The array to sum.

    Returns:
        int: The sum of the elements in the array.
    """
    calc = sum(array)
    return calc


if __name__ == "__main__":
    # Divide big_array into three sub-arrays
    data_array_division(big_array)

    # Calculate the sum of each sub-array concurrently
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit a task for each sub-array in divided_arrays
        results = [executor.submit(sum_of_array, array) for array in divided_arrays]

        # Retrieve the results as they complete
        for f in concurrent.futures.as_completed(results):
            summ_of_all_arrays.append(f.result())

    # Print the sum of all sub-arrays
    print(sum(summ_of_all_arrays))