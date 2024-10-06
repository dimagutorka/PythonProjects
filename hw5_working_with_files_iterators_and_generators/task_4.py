path_to_big_file = 'images_and_files/big_file'
path_to_filtered_file = 'images_and_files/only_lines_with_keyword'


def generator_of_lines_fromfile():
	with open(path_to_big_file, 'r') as fr:
		yield from fr.readlines()


def write_lines_by_keyword_infile(key_word):
	gen = generator_of_lines_fromfile()
	with open(path_to_filtered_file, 'w') as fw:
		for i in gen:
			if key_word in i:
				fw.write(i)


write_lines_by_keyword_infile('How')