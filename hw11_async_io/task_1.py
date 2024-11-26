import asyncio
from random import randint
from typing import List

# List of URLs to download
urls = ['www.url.com'] * 50


async def download_page(url: str) -> None:
    """
    Simulates downloading a page by waiting for a random period of time.

    Args:
        url (str): The URL of the page to download.

    This function simulates the asynchronous download of a web page.
    It randomly waits between 1 and 5 seconds to emulate a download delay.
    """
    # Generate a random delay time between 1 and 5 seconds
    time_to_wait = randint(1, 5)
    # Simulate the download delay asynchronously
    await asyncio.sleep(time_to_wait)
    # Print a message upon completion
    print(f"The page {url} has downloaded in {time_to_wait} seconds")


async def main(urls: List[str]) -> None:
    """
    Orchestrates the downloading of multiple pages asynchronously.

    This function creates a list of asynchronous download tasks for each URL
    and executes them concurrently using asyncio.gather.
    """
    # Create a list of tasks for each URL in the list
    task_list = [download_page(url) for url in urls]
    # Run all tasks concurrently and wait for their completion
    await asyncio.gather(*task_list)


# Entry point for asynchronous execution
if __name__ == '__main__':
    # Run the main asynchronous function with the list of URLs
    asyncio.run(main(urls))
