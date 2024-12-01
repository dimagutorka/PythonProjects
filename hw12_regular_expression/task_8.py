import re  # Module for regular expression operations

# Sample text to search in
text = "qwert AB12CD34 ggggg11111 "

# Regular expression pattern to match sequences like 'AB12CD34'
pattern = r'[A-Z]{2}[\d]{2}[A-Z]{2}[\d]{2}'


def text_in_string() -> bool:
	"""
	Searches for a specific pattern in the text and checks if it exists.

	Returns:
	bool: True if the pattern is found, False otherwise.
	"""
	# Find all occurrences of the pattern in the text
	word = re.findall(pattern, text)

	# If the pattern is found, return True; otherwise, return False
	if word:
		return True
	return False


# Print the result of the function, which checks if the pattern exists
print(text_in_string())
