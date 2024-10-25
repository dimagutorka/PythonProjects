class StringProcessor:
    """
    A class for performing various operations on a string, such as reversing,
    capitalizing, and counting vowels.

    Attributes:
        string (str): The string to be processed.
    """

    def __init__(self, string: str) -> None:
        """
        Initializes the StringProcessor with a string.

        Args:
            string (str): The string to be processed.
        """
        self.string = string

    def reverse_string(self) -> str:
        """
        Reverses the string.

        Returns:
            str: The reversed string.
        """
        return self.string[::-1]

    def capitalize_string(self) -> str:
        """
        Capitalizes the string (first character uppercase, others lowercase).

        Returns:
            str: The capitalized string.
        """
        return self.string.capitalize()

    def count_vowel(self) -> int:
        """
        Counts the number of vowels in the string.

        Returns:
            int: The count of vowels in the string.
        """
        vowels = "aeiouAEIOU"
        count = sum(self.string.count(vowel) for vowel in vowels)
        return count
