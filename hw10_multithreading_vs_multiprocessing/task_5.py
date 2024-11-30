import os
import concurrent.futures
from typing import List

# List all files in the 'big_files' directory
files: List[str] = os.listdir('big_files')


def search_in_file(file: str, keyword: str) -> List[str]:
    """
    Searches for a keyword in a file and records any matching lines.

    Args:
        file (str): The filename to search within the 'big_files' directory.
        keyword (str): The keyword to search for within the file.

    Returns:
        List[str]: A list of strings describing where the keyword was found within the file.
    """
    results = []

    # Open the file in read mode
    with open(f'big_files/{file}', 'r') as fr:
        # Enumerate each line to get line numbers
        for i, line in enumerate(fr):
            # Check if the keyword is in the line
            if keyword in line:
                results.append(f"The keyword \"{keyword}\" found in file \"{file}\" in line \"{i}\"")

    return results


if __name__ == '__main__':
    # Define the keyword to search for
    keyword_to_search = '171223-22:51:37:292'

    # Use ThreadPoolExecutor to search concurrently across multiple files
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit search tasks for each file in 'big_files'
        futures = [executor.submit(search_in_file, file=file, keyword=keyword_to_search) for file in files]

        # As each future completes, print the results
        for future in concurrent.futures.as_completed(futures):
            # Print each result line by line for each file
            for result in future.result():
                print(result)
