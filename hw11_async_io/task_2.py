import aiohttp
import asyncio
from typing import List

# List of URLs to be fetched
urls = ['https://skell.sketchengine.eu', 'https://www.python.org', 'https://www.github.com'] * 20


async def fetch_content(url: str, session: aiohttp.ClientSession) -> None:
    """
    Fetches content from a given URL asynchronously.

    Args:
        url (str): The URL to fetch content from.
        session (aiohttp.ClientSession): An aiohttp session object to manage connections.

    This function performs an asynchronous HTTP GET request to fetch the HTML content from
    the specified URL, prints the HTTP status, content type, and a snippet of the response body.
    It also includes error handling for connection errors, timeouts, and unexpected exceptions.
    """
    try:
        async with session.get(url) as response:
            html = await response.text()

            # Print status code, content type, and a preview of the body
            print('Status code:', response.status)
            print('Content type:', response.headers['content-type'])
            print("Body:", html[:15], "...")

    # Handle specific exceptions
    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"Connection error for {url}: {e}\n")

    except asyncio.TimeoutError:
        print(f"Request to {url} timed out")

    except Exception as e:
        print("An unexpected exception occurred:", e)


async def fetch_all(url_links: List[str]) -> None:
    """
    Orchestrates the fetching of content from multiple URLs asynchronously.

    Args:
        url_links (List[str]): A list of URLs to fetch content from.

    This function creates an aiohttp session to manage the requests and sends
    asynchronous fetch tasks for each URL using asyncio.gather to run them concurrently.
    """
    # Create a single session for all requests to reuse connections
    async with aiohttp.ClientSession() as session:
        # Prepare a list of tasks for fetching each URL's content
        task_list = [fetch_content(url, session) for url in url_links]
        # Run all tasks concurrently
        await asyncio.gather(*task_list)


# Entry point for asynchronous execution
asyncio.run(fetch_all(urls))
