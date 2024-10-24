import os
import concurrent.futures

files = os.listdir('big_files')


def search_in_file(file, keyword):
	results = []

	with open(f'big_files/{file}', 'r') as fr:
		for i, line in enumerate(fr):
			if keyword in line:
				results.append(f"The keyword \"{keyword}\" found in file \"{file}\" in line \"{i}\"")

	return results


if __name__ == '__main__':

	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = [executor.submit(search_in_file, file=file, keyword='171223-22:51:37:292') for file in files]

		for future in concurrent.futures.as_completed(futures):
			print(future.result())