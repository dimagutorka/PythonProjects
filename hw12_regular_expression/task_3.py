import concurrent.futures  # Module to handle multithreading
import re  # Module for working with regular expressions

# Path to the text file to be processed
file_path = 'text_files/text.txt'


def read_large_generator() -> str:
	"""
	Generator function to read a large file line by line.

	Yields:
	str: Each line of the file as a string.
	"""
	with open(file_path, 'r') as fr:
		for line in fr.readlines():  # Reads all lines and yields one by one
			yield line


def find_hashtag(line: str) -> list:
	"""
	Finds all hashtags in a given line using a regular expression.

	Parameters:
	line (str): The line of text to search for hashtags.

	Returns:
	list: A list of hashtags found in the line.
	"""
	return re.findall(r'#\w+', line)  # Matches any word starting with # and followed by letters/numbers


# Using a ThreadPoolExecutor to process lines concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
	# Map the find_hashtag function to each line read by the generator
	results = executor.map(find_hashtag, read_large_generator())

	# Print the results for each line (prints empty lists for lines without hashtags)
	for res in results:
		if res:  # Only print non-empty results to show lines with hashtags
			print(res)
