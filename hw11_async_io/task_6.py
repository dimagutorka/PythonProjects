import aiofiles
import aiohttp
import asyncio
import time

from hw10_multithreading_vs_multiprocessing.images_urls import urls


async def download_page(url, session):
	async with session.get(url) as response:
		image_content = await response.read()
		img_name = f'{url.split("/")[-1]}.jpg'

		async with aiofiles.open(f"images/{img_name}", 'wb') as img_file:
			await img_file.write(image_content)
			print(f'Photo {img_name} was downloaded and saved')


async def main(img_urls):
	async with aiohttp.ClientSession() as session:
		tasks_list = [download_page(img_url, session) for img_url in img_urls]
		await asyncio.gather(*tasks_list)

if __name__ == '__main__':
	asyncio.run(main(urls))

