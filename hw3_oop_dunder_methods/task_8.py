class Price:
    """A class to represent a price with support for basic arithmetic operations."""

    def __init__(self, price: float) -> None:
        """Initializes the Price with a rounded value.

        Args:
            price (float): The initial price value.
        """
        self.price = round(price, 2)  # Round to 2 decimal places

    def __add__(self, other: 'Price') -> float:
        """Adds two Price objects.

        Args:
            other (Price): The other Price object to add.

        Returns:
            float: The sum of the two prices.
        """
        return self.price + other.price

    def __sub__(self, other: 'Price') -> float:
        """Subtracts one Price object from another.

        Args:
            other (Price): The other Price object to subtract.

        Returns:
            float: The difference between the two prices.
        """
        return self.price - other.price

    def __eq__(self, other: 'Price') -> bool:
        """Checks if two Price objects are equal.

        Args:
            other (Price): The other Price object to compare.

        Returns:
            bool: True if both prices are equal, otherwise False.
        """
        return self.price == other.price


# Example usage
a = Price(200.5032545)
b = Price(100.25435453)
c = Price(200.5032545)

# Perform operations and comparisons
print("Addition:", a + b)          # Output: 300.76
print("Subtraction:", a - b)       # Output: 100.25
print("Equality a == b:", a == b)  # Output: False
print("Equality a == c:", a == c)  # Output: True
