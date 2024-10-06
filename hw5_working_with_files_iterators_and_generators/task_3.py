from PIL import Image
import os


absolute_path = '/Users/cblpok/Documents/GitHub/PythonProjects/hw5_working_with_files_iterators_and_generators/pictures_for_task3/'
images_formats = ['.png', '.jpg']
list_of_files = os.listdir("pictures_for_task3")


def all_images_in_directory(formats, files):
	list_of_all_images = []
	for i in formats:
		for j in files:
			if i in j:
				list_of_all_images.append(j)
	return list_of_all_images


list_of_images = all_images_in_directory(images_formats, list_of_files)
iterable_object = iter(list_of_images)

counter = 0

with open('pictures_for_task3/text.csv', 'w') as f:
	while True:
		counter += 1
		if counter <= len(list_of_images):
			img = Image.open(f"{absolute_path}{next(iterable_object)}", 'r')
			string_with_meta_data_of_image = f'Size - {img.size} \nFormat - {img.format} \nFile name - {img.filename}'
			f.write(f'Image #{counter} \n')
			f.write(f'{string_with_meta_data_of_image}' + 3 * '\n')

		else:
			break
