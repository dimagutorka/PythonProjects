from PIL import Image
import os
from typing import List

# Absolute path to the directory containing images
absolute_path = '/Users/cblpok/Documents/GitHub/PythonProjects/' \
                'hw5_working_with_files_iterators_and_generators/pictures_for_task3/'
images_formats = ['.png', '.jpg']
list_of_files = os.listdir("pictures_for_task3")


def all_images_in_directory(formats: List[str], files: List[str]) -> List[str]:
    """Retrieves a list of all image files in the specified directory with the given formats.

    Args:
        formats (List[str]): A list of image formats to filter by (e.g., '.png', '.jpg').
        files (List[str]): A list of file names in the directory.

    Returns:
        List[str]: A list of file names that match the specified formats.
    """
    list_of_all_images = []
    for fmt in formats:
        for file in files:
            if fmt in file:
                list_of_all_images.append(file)
    return list_of_all_images


# Get all images in the directory with the specified formats
list_of_images = all_images_in_directory(images_formats, list_of_files)
iterable_object = iter(list_of_images)

counter = 0

# Create or overwrite a CSV file and write image metadata
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
