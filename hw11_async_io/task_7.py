import asyncio
import aiohttp
import requests
import concurrent.futures
import time
from multiprocessing import Pool

urls = ['https://superfastpython.com/asyncio-wait_for/'] * 100


def time_consume_counter(func):
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		func()
		end = time.perf_counter()
		print(f"{end - start:.2f} seconds")

	return wrapper


def send_request(url, ind):
	response = requests.get(url)
	return response


@time_consume_counter
def requests_via_multi_threads():
	with concurrent.futures.ThreadPoolExecutor() as executor:
		tasks = [executor.submit(send_request, url, ind) for ind, url in enumerate(urls)]

	print(f"MULTITHREADING --> 100 out of {len(tasks)} requests were finished in ", end='')


@time_consume_counter
def requests_via_multi_processes():
	with Pool(processes=20) as pool:
		results = pool.starmap(send_request, zip(urls, list(range(0, 100))))

	print(f"MULTIPROCESSING --> 100 out of {len(results)} processes were finished in ", end='')


async def make_async_request(url, session):
	async with session.get(url) as response:
		await response.text()


async def send_async_request(url_links):
	async with aiohttp.ClientSession() as session:
		task_list = [make_async_request(url, session) for url in url_links]

		start = time.perf_counter()
		await asyncio.gather(*task_list)
		end = time.perf_counter()

		print(f"ASYNC --> 100 out of {len(task_list)} processes were finished in {end - start:.2f} seconds")


@time_consume_counter
def send_request_sync():
	for ind, url in enumerate(urls):
		send_request(url, ind)

	print(f"SYNC --> 100 out of 100 processes were finished in ", end='')


if __name__ == '__main__':
	asyncio.run(send_async_request(urls))
	#  ASYNC --> 100 out of 100 processes were finished in 0.98 seconds

	time.sleep(2)
	requests_via_multi_processes()
	#  MULTIPROCESSING --> 100 out of 100 processes were finished in 3.61 seconds

	time.sleep(2)
	requests_via_multi_threads()
	#  MULTITHREADING --> 100 out of 100 requests were finished in 2.79 seconds

	time.sleep(2)
	send_request_sync()
#  SYNC --> 100 out of 100 processes were finished in 30.35 seconds
