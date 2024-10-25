import concurrent.futures
import time
from PIL import Image
import os
from typing import List

# Get a list of all image file names in the specified directory
images_path: List[str] = os.listdir("images_for_correction")


def image_correction(img_name: str) -> None:
    """
    Applies a cropping and color channel swap to the given image, then saves the result.

    Args:
        img_name (str): The filename of the image to process.

    This function opens an image, crops it to a 500x500 pixel box, and swaps
    the red and blue color channels. The processed image is saved with a new
    filename in the same directory.
    """
    # Define the box for cropping (top-left corner (0,0) to (500,500))
    box = (0, 0, 500, 500)
    # Open the image
    im = Image.open(f'images_for_correction/{img_name}')
    # Crop the image to the defined box
    reg = im.crop(box)
    # Split the image into its color channels
    r, g, b = reg.split()
    # Merge the channels back, swapping red and blue
    reg = Image.merge("RGB", (b, g, r))
    # Save the modified image
    reg.save(f'images_for_correction/copy_{img_name}.jpg')


if __name__ == '__main__':
    # Start the performance timer
    start = time.perf_counter()

    # Use a ThreadPoolExecutor to process images concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Apply image_correction to each image in the images_path list
        executor.map(image_correction, images_path)

    # End the performance timer
    end = time.perf_counter()
    print(f"Process finished in {end - start:.2f} seconds")
