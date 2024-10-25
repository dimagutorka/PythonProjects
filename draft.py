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
		print(f"requests finished in {end - start:.2f} seconds")

	return wrapper


def send_request(url, ind):
	response = requests.get(url)
	return response


def requests_via_multi_threads():
	start = time.perf_counter()

	with concurrent.futures.ThreadPoolExecutor() as executor:
		tasks = [executor.submit(send_request, url, ind) for ind, url in enumerate(urls)]

	end = time.perf_counter()
	print(f"MULTITHREADING --> 100 out of {len(tasks)} requests were finished in {end - start:.2f} seconds")


def requests_via_multi_processes():
	start = time.perf_counter()

	with Pool(processes=20) as pool:
		results = pool.starmap(send_request, zip(urls, list(range(0, 100))))

	end = time.perf_counter()
	print(f"MULTIPROCESSING --> 100 out of {len(results)} processes were finished in {end - start:.2f} seconds")


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


def send_request_sync():
	start = time.perf_counter()

	for ind, url in enumerate(urls):
		send_request(url, ind)

	end = time.perf_counter()
	print(f"SYNC --> 100 out of 100 processes were finished in {end - start:.2f} seconds")


if __name__ == '__main__':
	asyncio.run(send_async_request(urls))
	#  ASYNC --> 100 out of 100 processes were finished in 0.98 seconds

	time.sleep(4)
	requests_via_multi_processes()
	#  MULTIPROCESSING --> 100 out of 100 processes were finished in 3.61 seconds

	time.sleep(4)
	requests_via_multi_threads()
	#  MULTITHREADING --> 100 out of 100 requests were finished in 2.79 seconds

	time.sleep(4)
	send_request_sync()
	#  SYNC --> 100 out of 100 processes were finished in 30.35 seconds
