from zipfile import ZipFile
import os
from typing import List

# Directory to be archived
directory = './files_to_archive_task10'
file_paths: List[str] = []

def get_all_file_paths(directory: str) -> None:
    """Recursively retrieves all file paths in the specified directory and adds them to the file_paths list.

    Args:
        directory (str): The directory to search for files.
    """
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

def archive_file(path_to_archive: str) -> None:
    """Creates a zip archive of all files in the specified directory.

    Args:
        path_to_archive (str): The path to the zip file to create.
    """
    with ZipFile(path_to_archive, 'w') as zip:
        get_all_file_paths(directory)
        for file in file_paths:
            zip.write(file, os.path.relpath(file, directory))  # Store file with relative path


# Example usage
archive_file('archives_task10/my_python_files.zip')
