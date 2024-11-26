import re  # Module for regular expression operations
import concurrent.futures  # Module for concurrent execution using threads


def phone_number_filter() -> str:
    """
    Generator function to read a file line by line.

    Yields:
    str: Each line from the file as a string.
    """
    with open('text_files/numbers.txt', 'r') as fr:
        for line in fr.readlines():  # Reads all lines and yields them one by one
            yield line


def is_valid_number(line: str) -> list:
    """
    Finds and returns valid phone numbers in a line of text.

    Parameters:
    line (str): The line of text to search for phone numbers.

    Returns:
    list: A list of matched phone numbers, or None if no matches are found.
    """
    # Pattern to match different phone number formats:
    # - 10-digit numbers (e.g., "1234567890")
    # - Numbers with area code in parentheses and a space (e.g., "(123) 456-7890")
    # - Numbers with dots as separators (e.g., "123.456.7890")
    # - Numbers with dashes as separators (e.g., "123-456-7890")
    pattern: str = r'([0-9]{10}|[(][0-9]{3}[)][\s][0-9]{3}-[0-9]{4}|[0-9]{3}[.][0-9]{3}[.][0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})'
    matched_number = re.findall(pattern, line)  # Finds all occurrences that match the pattern in the line

    # Return the list of matched numbers if found
    if matched_number:
        return matched_number


# Use a ThreadPoolExecutor to concurrently process lines from the file
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Map the is_valid_number function to each line produced by phone_number_filter
    results = executor.map(is_valid_number, phone_number_filter())

    # Print each result if a valid phone number is found
    for number in results:
        if number:  # Print only non-empty results
            print(number)
