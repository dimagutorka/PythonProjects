import asyncio
import aiohttp
import requests
import concurrent.futures
import time

from multiprocessing import Pool
from typing import Callable, List

# List of URLs to send requests to
urls = ['https://superfastpython.com/asyncio-wait_for/'] * 100


def time_consume_counter(func: Callable) -> Callable:
    """
    Decorator to measure the execution time of a function.

    Args:
        func (Callable): The function whose execution time is measured.

    Returns:
        Callable: Wrapped function with execution time measurement.
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{end - start:.2f} seconds")

    return wrapper


def send_request(url: str, ind: int) -> requests.Response:
    """
    Sends a synchronous HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the request to.
        ind (int): The index of the request.

    Returns:
        requests.Response: The response object from the request.
    """
    response = requests.get(url)
    return response


@time_consume_counter
def requests_via_multi_threads() -> None:
    """
    Sends multiple requests using multithreading to handle 100 concurrent requests.

    This function uses ThreadPoolExecutor to create threads for sending requests concurrently.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tasks = [executor.submit(send_request, url, ind) for ind, url in enumerate(urls)]

    print(f"MULTITHREADING --> 100 out of {len(tasks)} requests were finished in ", end='')


@time_consume_counter
def requests_via_multi_processes() -> None:
    """
    Sends multiple requests using multiprocessing to handle 100 concurrent requests.

    This function uses a multiprocessing pool to distribute requests among processes.
    """
    with Pool(processes=20) as pool:
        results = pool.starmap(send_request, zip(urls, list(range(0, 100))))

    print(f"MULTIPROCESSING --> 100 out of {len(results)} processes were finished in ", end='')


async def make_async_request(url: str, session: aiohttp.ClientSession) -> None:
    """
    Sends an asynchronous HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the request to.
        session (aiohttp.ClientSession): The aiohttp session for making requests.
    """
    async with session.get(url) as response:
        await response.text()


async def send_async_request(url_links: List[str]) -> None:
    """
    Sends multiple requests asynchronously using asyncio and aiohttp.

    Args:
        url_links (List[str]): A list of URLs to send requests to.
    """
    async with aiohttp.ClientSession() as session:
        task_list = [make_async_request(url, session) for url in url_links]

        start = time.perf_counter()
        await asyncio.gather(*task_list)
        end = time.perf_counter()

        print(f"ASYNC --> 100 out of {len(task_list)} processes were finished in {end - start:.2f} seconds")


@time_consume_counter
def send_request_sync() -> None:
    """
    Sends multiple requests synchronously in a loop to handle 100 requests sequentially.
    """
    for ind, url in enumerate(urls):
        send_request(url, ind)

    print(f"SYNC --> 100 out of 100 processes were finished in ", end='')


if __name__ == '__main__':
    # Run asynchronous requests
    asyncio.run(send_async_request(urls))

    time.sleep(2)  # Pause before running the next function
    requests_via_multi_processes()

    time.sleep(2)
    requests_via_multi_threads()

    time.sleep(2)
    send_request_sync()
