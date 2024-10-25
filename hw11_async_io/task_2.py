import aiohttp
import asyncio

urls = ['https://skell.sketchengine.eu', 'https://www.python.org', 'https://www.github.com','https://skell.sketchengine.eu', 'https://www.python.org', 'https://www.github.com','https://skell.sketchengine.eu', 'https://www.python.org', 'https://www.github.com','https://skell.sketchengine.eu', 'https://www.python.org', 'https://www.github.com','https://skell.sketchengine.eu', 'https://www.python.org', 'https://www.github.com']


async def fetch_content(url, session):
	try:
		async with session.get(url) as response:
			html = await response.text()

			print('Status code', response.status)
			print('Content type', response.headers['content-type'])
			print("Body:", html[:15], "...")

	except aiohttp.client_exceptions.ClientConnectorError as e:
		print(f"Connection error for {url}: {e} \n")

	except asyncio.TimeoutError as e:
		print(f"Request to {url} times out")

	except Exception as e:
		print("An unexpected exception occurred")


async def fetch_all(url_links):
	async with aiohttp.ClientSession() as session:
		task_list = [fetch_content(url, session) for url in url_links]
		await asyncio.gather(*task_list)


asyncio.run(fetch_all(urls))
