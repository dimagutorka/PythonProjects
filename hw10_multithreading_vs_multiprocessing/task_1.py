import threading
import time
import requests
from typing import Callable
from images_urls import urls  # Import the list of image URLs

def download(url: str) -> None:
    """
    Downloads an image from a URL and saves it to the 'images' directory.

    Args:
        url (str): The URL of the image to download.

    This function sends an HTTP GET request to fetch the image content and
    saves it as a .jpg file in the 'images' directory, with a filename based on the image URL.
    """
    img_bytes = requests.get(url).content
    img_name = url.split("/")[-1]
    img_name = f'{img_name}.jpg'

    with open(f"images/{img_name}", 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'Photo {img_name} was downloaded and saved')


def time_consume_counter(func: Callable) -> Callable:
    """
    Decorator to measure the execution time of a function.

    Args:
        func (Callable): The function whose execution time is measured.

    Returns:
        Callable: Wrapped function that measures and prints execution time.
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Process finished in {end - start:.2f} seconds")

    return wrapper


@time_consume_counter
def thread_creation() -> None:
    """
    Creates and starts a thread for each image download.

    This function iterates through a list of image URLs, creating a separate
    thread for each download. It then waits for all threads to complete before
    finishing execution.
    """
    threads = []
    for url in urls:
        # Create and start a new thread for each download task
        t = threading.Thread(target=download, args=(url,))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    thread_creation()
