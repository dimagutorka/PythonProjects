def even_number_generator():
	number = 0
	while True:
		yield number
		number += 2


file_name = 'limited_generator/even_numbers_from_generator'


def file(path, limit=100):
	gen = even_number_generator()

	with open(path, 'w') as fw:
		for i in range(limit):
			fw.write(f'{next(gen)} \n')


file(file_name, 100)