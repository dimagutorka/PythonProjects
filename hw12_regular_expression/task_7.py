import concurrent.futures  # Module for concurrent execution using threads
import re  # Module for working with regular expressions


def read_large_file_generator() -> str:
	"""
	Generator function to read a file line by line.

	Yields:
	str: Each line from the file as a string.
	"""
	with open('text_files/file_with_ip_address.txt', 'r') as fr:
		for line in fr:
			yield line  # Yield each line one by one to be processed


def is_valid_ip(line: str) -> list:
	"""
	Finds all valid IP addresses in a line of text using a regular expression.

	Parameters:
	line (str): The line of text to search for IP addresses.

	Returns:
	list: A list of valid IP addresses found in the line, or None if no matches are found.
	"""
	# Regular expression pattern to match valid IPv4 addresses
	pattern = (
		r'(?:25[0-5][.]|2[0-4][0-9][.]|1[0-9]{2}[.]|[1-9]?[0-9][.]){3}'
		r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
	)

	# Find all occurrences of the pattern in the line
	matching = re.findall(pattern, line)

	if matching:
		return matching  # Return the list of matched IP addresses


# Use a ThreadPoolExecutor to process lines concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
	# Map the is_valid_ip function to each line generated by read_large_file_generator
	results = executor.map(is_valid_ip, read_large_file_generator())

	# Print the results if a valid IP address is found in the line
	for res in results:
		if res:  # Only print non-empty results
			print(res)