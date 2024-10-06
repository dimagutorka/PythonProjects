path_to_log = 'log_files/log_file.log'
path_to_errors = 'log_files/errors_only'


def generator(path_log_file):
	with open(path_log_file, 'r') as fr:
		yield from fr.readlines()


def error_filter(path_to_error_file):
	gen = generator(path_to_log)
	with open(path_to_error_file, 'w') as fw:

		for i in gen:
			if 'error' in i:
				fw.write(i)


error_filter(path_to_errors)