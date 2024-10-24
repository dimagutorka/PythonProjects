import threading
import time
import requests
from images_urls import urls

images_names = []


def download(url):
	img_bytes = requests.get(url).content
	img_name = url.split("/")[-1]
	img_name = f'{img_name}.jpg'
	images_names.append(img_name)
	with open(f"images/{img_name}", 'wb') as img_file:
		img_file.write(img_bytes)
		print(f'Photo {img_name} was downloaded and saved')


def time_consume_counter(func):

	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		func()
		end = time.perf_counter()
		print(f"Process finished in {end - start:.2f} seconds")

	return wrapper


@time_consume_counter
def thread_creation():
	threads = []
	for url in (urls):
		t = threading.Thread(target=download, args=(url,))
		t.start()
		threads.append(t)

	for i in threads:
		i.join()


if __name__ == '__main__':
	thread_creation()

