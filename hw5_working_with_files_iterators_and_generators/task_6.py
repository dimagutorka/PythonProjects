import os

directory_to_files = 'pictures_for_task3'


def directory_files(path_to_directory):
	list_of_dirs = os.listdir(path_to_directory)
	iterable_object = iter(list_of_dirs)

	counter = len(list_of_dirs)

	while counter != 0:
		counter -= 1
		iteration = next(iterable_object)
		path_to_file = f'{path_to_directory}/{iteration}'

		print(f'Name of a file - {iteration}')
		print(f'Size of a file - {os.path.getsize(path_to_file)}')
		print('-' * 20)


directory_files(directory_to_files)
