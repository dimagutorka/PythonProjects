import aiofiles
import aiohttp
import asyncio
from typing import List

# Import the list of image URLs
from hw10_multithreading_vs_multiprocessing.images_urls import urls


async def download_page(url: str, session: aiohttp.ClientSession) -> None:
    """
    Downloads an image from a URL and saves it to the 'images' directory.

    Args:
        url (str): The URL of the image to download.
        session (aiohttp.ClientSession): The aiohttp session for making HTTP requests.

    This function performs an asynchronous HTTP GET request to fetch the image data,
    then saves the data as a .jpg file in the 'images' directory with a name based
    on the image URL.
    """
    async with session.get(url) as response:
        # Read the binary content of the image
        image_content = await response.read()
        # Extract image name from URL
        img_name = f'{url.split("/")[-1]}.jpg'

        # Save the image content to a file asynchronously
        async with aiofiles.open(f"images/{img_name}", 'wb') as img_file:
            await img_file.write(image_content)
            print(f'Photo {img_name} was downloaded and saved')


async def main(img_urls: List[str]) -> None:
    """
    Manages the asynchronous downloading of images from a list of URLs.

    Args:
        img_urls (List[str]): A list of URLs for images to be downloaded.

    This function creates an aiohttp session and uses asyncio.gather to
    download multiple images concurrently, enhancing performance by
    utilizing asynchronous I/O.
    """
    async with aiohttp.ClientSession() as session:
        # Create a list of download tasks for each URL
        tasks_list = [download_page(img_url, session) for img_url in img_urls]
        # Run all tasks concurrently
        await asyncio.gather(*tasks_list)


# Entry point for asynchronous execution
if __name__ == '__main__':
    asyncio.run(main(urls))
