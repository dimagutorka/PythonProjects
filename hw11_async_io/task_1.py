import asyncio
import time
from random import randint

urls = ['www.url.com', 'www.url1.com', 'www.url2.com','www.url3.com','www.url4.com','www.url5.com','www.url6.com','www.url7.com']


async def download_page(url):
	time_to_wait = randint(1, 5)
	await asyncio.sleep(time_to_wait)
	print(f"The page {url} has downloaded in {time_to_wait} seconds")


async def main(urls):
	task_list = [download_page(url) for url in urls]
	await asyncio.gather(*task_list)


if __name__ == '__main__':
	asyncio.run(main(urls))
