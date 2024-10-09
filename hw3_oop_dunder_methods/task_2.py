class Vector:
    """A class to represent a mathematical vector."""

    def __init__(self, point: float) -> None:
        """Initializes the Vector with a given point.

        Args:
            point (float): The numerical value representing the point of the vector.
        """
        self.point = point

    def __add__(self, other: 'Vector') -> float:
        """Adds two vectors.

        Args:
            other (Vector): The vector to add.

        Returns:
            float: The result of adding the two vectors.
        """
        return self.point + other.point

    def __sub__(self, other: 'Vector') -> float:
        """Subtracts one vector from another.

        Args:
            other (Vector): The vector to subtract.

        Returns:
            float: The result of the subtraction.
        """
        return self.point - other.point

    def __mul__(self, other: 'Vector') -> float:
        """Multiplies two vectors.

        Args:
            other (Vector): The vector to multiply.

        Returns:
            float: The result of multiplying the two vectors.
        """
        return self.point * other.point

    def __lt__(self, other: 'Vector') -> bool:
        """Compares two vectors to determine if one is less than the other.

        Args:
            other (Vector): The vector to compare.

        Returns:
            bool: True if the current vector is less than the other vector.
        """
        return self.point < other.point

    def __eq__(self, other: 'Vector') -> bool:
        """Checks if two vectors are equal.

        Args:
            other (Vector): The vector to compare.

        Returns:
            bool: True if the two vectors are equal.
        """
        return self.point == other.point

    def get_vector_length(self) -> str:
        """Returns the length of the vector as a string.

        Returns:
            str: A string representation of the vector's length.
        """
        return f"The length of the vector is {self.point}"


# Example usage
a = Vector(1)
b = Vector(5)

add1 = a + b
sub1 = a - b
mul1 = a * b
lt1 = a < b
eq1 = a == b

print("Addition:", add1)        # Output: 6
print("Subtraction:", sub1)     # Output: -4
print("Multiplication:", mul1)  # Output: 5
print("Less Than:", lt1)        # Output: True
print("Equal:", eq1)            # Output: False

print(a.get_vector_length())    # Output: "The length of the vector is 1"
