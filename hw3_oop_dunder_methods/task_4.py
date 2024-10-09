class BinaryNumber:
    """A class to represent binary numbers and perform bitwise operations."""

    def __init__(self, x: int) -> None:
        """Initializes the BinaryNumber with an integer value.

        Args:
            x (int): The integer value representing the binary number.
        """
        self.x = x

    def __and__(self, other: 'BinaryNumber') -> int:
        """Performs a bitwise AND operation between two BinaryNumber instances.

        Args:
            other (BinaryNumber): The other BinaryNumber to AND with.

        Returns:
            int: The result of the bitwise AND operation.
        """
        return self.x & other.x

    def __or__(self, other: 'BinaryNumber') -> int:
        """Performs a bitwise OR operation between two BinaryNumber instances.

        Args:
            other (BinaryNumber): The other BinaryNumber to OR with.

        Returns:
            int: The result of the bitwise OR operation.
        """
        return self.x | other.x

    def __xor__(self, other: 'BinaryNumber') -> int:
        """Performs a bitwise XOR operation between two BinaryNumber instances.

        Args:
            other (BinaryNumber): The other BinaryNumber to XOR with.

        Returns:
            int: The result of the bitwise XOR operation.
        """
        return self.x ^ other.x

    def __invert__(self) -> int:
        """Performs a bitwise NOT operation on the BinaryNumber instance.

        Returns:
            int: The result of the bitwise NOT operation.
        """
        return ~self.x

# Example usage
a = BinaryNumber(32)  # Binary representation: 100000
b = BinaryNumber(16)  # Binary representation: 010000

print("Bitwise AND:", a & b)  # Output: 0 (Binary: 000000)
print("Bitwise OR:", a | b)   # Output: 48 (Binary: 110000)
print("Bitwise XOR:", a ^ b)  # Output: 48 (Binary: 110000)
print("Bitwise NOT:", ~a)      # Output: -33 (Binary: 11111111111111111111111111111111111111111111111111111111111111000)
