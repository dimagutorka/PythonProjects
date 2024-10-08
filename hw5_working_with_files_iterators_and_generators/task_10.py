from zipfile import ZipFile
import os


directory = './files_to_archive_task10'
file_paths = []


def get_all_file_paths(directory):
	for root, directories, files in os.walk(directory):
		for filename in files:
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)


def archive_file(path_to_archive):
	with ZipFile(path_to_archive, 'w') as zip:
		get_all_file_paths(directory)
		for file in file_paths:
			zip.write(file)


archive_file('archives_task10/my_python_files.zip')
