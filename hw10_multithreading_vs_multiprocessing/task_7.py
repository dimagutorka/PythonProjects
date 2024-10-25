import concurrent.futures
import functools
import numpy as np
from typing import List

# List to store partial factorial results
summa: List[int] = []


def divide_into_small_factorials(array: np.ndarray) -> List[int]:
    """
    Computes the product of elements in the input array (sub-factorial) and returns it in a list.

    Args:
        array (np.ndarray): The sub-array of integers to compute the factorial product.

    Returns:
        List[int]: A list containing the product of the elements in the input array.
    """
    # Compute the factorial of the sub-array using functools.reduce
    sub_factor = functools.reduce(lambda x, y: x * y, array)
    return [sub_factor]


def factorial() -> int:
    """
    Calculates the product of all elements in 'summa' to yield the final factorial result.

    Returns:
        int: The factorial result after combining all sub-factorials in 'summa'.
    """
    # Multiply all sub-factorials to get the final factorial
    factor_result = functools.reduce(lambda x, y: x * y, summa)
    return factor_result


if __name__ == "__main__":
    # Start the multiprocessing execution
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Get user input for the number of sections and the factorial number
        sections_to_divide = int(input('Enter the number of sections to divide the process: '))
        factor = int(input('Enter the factorial to compute: '))

        # Split the range of numbers into smaller sub-arrays for parallel processing
        sub_arrays = np.array_split(list(range(1, factor + 1)), sections_to_divide)

        # Submit each sub-array to the process pool for parallel computation
        futures = [executor.submit(divide_into_small_factorials, array=sub_array) for sub_array in sub_arrays]

        # Collect results from each future as they complete
        for future in futures:
            summa.append(future.result()[0])

    # Compute the final factorial by combining all partial results
    print(factorial())
