from fractions import Fraction as F  # Importing the built-in Fraction class

class Fraction:
    """A class to represent fractions and perform arithmetic operations on them."""

    def __init__(self, number: float) -> None:
        """Initializes the Fraction with a floating-point number.

        Args:
            number (float): The number to be represented as a fraction.
        """
        self.number = F(number)  # Use the built-in Fraction class for precise arithmetic

    def __str__(self) -> str:
        """Returns a string representation of the fraction.

        Returns:
            str: A string representing the fraction in the form 'numerator / denominator'.
        """
        return f"{self.number.numerator} \n" + '-' * len(str(self.number.denominator)) + f"\n{self.number.denominator}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Adds two fractions.

        Args:
            other (Fraction): The other fraction to add.

        Returns:
            Fraction: The sum of the two fractions.
        """
        result = self.number + other.number
        return Fraction(result)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Subtracts one fraction from another.

        Args:
            other (Fraction): The fraction to subtract.

        Returns:
            Fraction: The difference between the two fractions.
        """
        result = self.number - other.number
        return Fraction(result)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Multiplies two fractions.

        Args:
            other (Fraction): The other fraction to multiply.

        Returns:
            Fraction: The product of the two fractions.
        """
        result = self.number * other.number
        return Fraction(result)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Divides one fraction by another.

        Args:
            other (Fraction): The fraction to divide by.

        Returns:
            Fraction: The quotient of the two fractions.
        """
        result = self.number / other.number
        return Fraction(result)

# Example usage
a = Fraction(0.1)
b = Fraction(0.5)

print("Addition:")
print(a + b)  # Output: Fraction representing 0.6

print("\nSubtraction:")
print(a - b)  # Output: Fraction representing -0.4

print("\nMultiplication:")
print(a * b)  # Output: Fraction representing 0.05

print("\nDivision:")
print(a / b)  # Output: Fraction representing 0.2
