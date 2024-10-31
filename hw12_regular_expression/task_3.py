import concurrent.futures
import re

file_path = 'text_files/text.txt'


def read_large_generator():
	with open(file_path, 'r') as fr:
		for line in fr.readlines():
			yield line


def find_hashtag(line):
	return re.findall(r'#\w+', line)


with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
	results = executor.map(find_hashtag, read_large_generator())

	for res in results:
		print(res)