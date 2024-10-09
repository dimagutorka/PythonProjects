def string_upper(string: str) -> str:
    """Converts a given string to uppercase and removes leading/trailing whitespace.

    Args:
        string (str): The input string to be processed.

    Returns:
        str: The uppercase version of the input string with whitespace removed.
    """
    return string.upper().strip()


# Example usage
result = string_upper("   hello world   ")
print(result)  # Output: "HELLO WORLD"
