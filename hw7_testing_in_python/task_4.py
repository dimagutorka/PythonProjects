import doctest

def is_even(n: int) -> bool:
    """
    Checks if a number is even.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if the number is even, False otherwise.

    Examples:
        >>> is_even(2)
        True
        >>> is_even(1)
        False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Computes the factorial of a number.

    Args:
        n (int): The integer for which to calculate the factorial. Must be greater than 0.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If n is less than or equal to 0.

    Examples:
        >>> factorial(1)
        1
        >>> factorial(5)
        120
        >>> factorial(0)
        Traceback (most recent call last):
            ...
        ValueError: n should be greater than 0
    """
    if n == 1:
        return 1
    elif n <= 0:
        raise ValueError("n should be greater than 0")
    return factorial(n - 1) * n


if __name__ == '__main__':
    doctest.testmod()
