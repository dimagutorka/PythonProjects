def factorial(n: int) -> int:
    """Calculates the factorial of a given number using recursion.

    Args:
        n (int): The number to calculate the factorial for. Must be a positive integer.

    Returns:
        int: The factorial of the given number.

    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    if n == 1 or n == 0:  # Handle 0! case
        return 1
    return factorial(n - 1) * n


def the_largest_common_divisor(number_1: int, number_2: int) -> int:
    """Finds the largest common divisor (the greatest common divisor) of two numbers.

    Args:
        number_1 (int): The first number.
        number_2 (int): The second number.

    Returns:
        int: The largest common divisor of the two numbers.
    """
    the_largest_number = max(number_1, number_2)
    the_largest_divisor = 0

    for i in range(1, the_largest_number + 1):  # Include the largest number itself
        if number_1 % i == 0 and number_2 % i == 0:
            the_largest_divisor = i

    return the_largest_divisor


# Example usage
print(factorial(5))  # Output: 120
print(the_largest_common_divisor(28, 42))  # Output: 14
