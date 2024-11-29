import re  # Regular expressions for pattern matching
import requests  # For sending HTTP requests

# Send a GET request to the URL and store the response
r = requests.get('https://www.englishpage.com/modals/hadbetter.html')


def remove_html_tags() -> str:
	"""
	Removes HTML tags from the content of the webpage.

	Returns:
	str: The text content of the webpage with HTML tags removed.
	"""
	# Regex pattern to match any HTML tag
	pattern = r'<.*?>'

	# Substitute matched HTML tags with an empty string
	cleantext = re.sub(pattern, '', r.text)

	return cleantext


# Print the cleaned content
print(remove_html_tags())
