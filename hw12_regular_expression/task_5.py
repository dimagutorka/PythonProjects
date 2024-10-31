import re
import requests


r = requests.get('https://www.englishpage.com/modals/hadbetter.html')


def remove_html_tags():
	pattern = r'<.*?>'
	cleantext = re.sub(pattern, '', r.text)

	return cleantext


print(remove_html_tags())