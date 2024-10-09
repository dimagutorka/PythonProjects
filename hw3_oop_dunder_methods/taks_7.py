class Vector:
    """A class to represent a 2D vector with x and y components."""

    def __init__(self, x: float, y: float) -> None:
        """Initializes the Vector with x and y components.

        Args:
            x (float): The x component of the vector.
            y (float): The y component of the vector.
        """
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        """Adds two vectors.

        Args:
            other (Vector): The other vector to add.

        Returns:
            Vector: A new Vector that is the sum of the two vectors.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtracts one vector from another.

        Args:
            other (Vector): The vector to subtract.

        Returns:
            Vector: A new Vector that is the difference of the two vectors.
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vector') -> float:
        """Calculates the dot product of two vectors.

        Args:
            other (Vector): The other vector to multiply.

        Returns:
            float: The dot product of the two vectors.
        """
        return self.x * other.x + self.y * other.y

    def __eq__(self, other: 'Vector') -> bool:
        """Checks if two vectors are equal.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if the two vectors are equal, False otherwise.
        """
        return self.x == other.x and self.y == other.y

# Example usage
vector_a = Vector(10, 5)
vector_b = Vector(20, 10)

# Operations with x components
print("X Component Operations:")
print("Addition:", vector_a.x + vector_b.x)   # Output: 30
print("Subtraction:", vector_a.x - vector_b.x)  # Output: -10
print("Dot Product (as multiplication):", vector_a.x * vector_b.x)  # Output: 200
print("Equality Check:", vector_a.x == vector_b.x)  # Output: False

print("\nY Component Operations:")
print("Addition:", vector_a.y + vector_b.y)   # Output: 15
print("Subtraction:", vector_a.y - vector_b.y)  # Output: -5
print("Dot Product (as multiplication):", vector_a.y * vector_b.y)  # Output: 50
print("Equality Check:", vector_a.y == vector_b.y)  # Output: False
