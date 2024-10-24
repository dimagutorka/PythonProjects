import concurrent.futures
import time

from PIL import Image
import os

images_path = os.listdir("images_for_correction")


def image_correction(img_name):
	box = (0, 0, 500, 500)
	im = Image.open(f'images_for_correction/{img_name}')
	reg = im.crop(box)
	r, g, b = reg.split()
	reg = Image.merge("RGB", (b, g, r))
	reg.save(f'images_for_correction/copy_{img_name}.jpg')


if __name__ == '__main__':
	start = time.perf_counter()

	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(image_correction, images_path)

	end = time.perf_counter()
	print(f"Process finished in {end - start:.2f} seconds")