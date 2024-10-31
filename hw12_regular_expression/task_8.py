import re

text = "qwert AB12CD34 ggggg11111 "
pattern = r'[A-Z]{2}[\d]{2}[A-Z]{2}[\d]{2}'


def text_in_string():
	word = re.findall(pattern, text)
	if word:
		return True
	return False


print(text_in_string())

