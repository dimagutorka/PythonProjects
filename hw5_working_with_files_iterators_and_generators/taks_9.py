import shutil
import os


class BackUpCopies:
    """A context manager for creating backup copies of a specified file.

    Attributes:
        path_to_original_file (str): The path to the original file to back up.
        backup_file (str): The path to the backup file location.
    """

    path_to_original_file: str = 'original_file_task9/text2'
    backup_file: str = 'backup_copies_task9/new_copy'

    def __init__(self, filename: str, mode: str) -> None:
        """Initializes the BackUpCopies object.

        Args:
            filename (str): The name of the backup file to open.
            mode (str): The mode for opening the file ('r' for reading, 'w' for writing).
        """
        self.filename = filename
        self.mode = mode
        self.file = None

    @classmethod
    def set_paths(cls, file_to_backup: str, destination_directory: str) -> None:
        """Sets the paths for the original file and the backup file.

        Args:
            file_to_backup (str): The path to the file to back up.
            destination_directory (str): The path where the backup will be stored.
        """
        cls.path_to_original_file = file_to_backup
        cls.backup_file = destination_directory

    def __enter__(self) -> 'TextIOWrapper':
        """Creates a backup of the original file and opens the backup file.

        Returns:
            TextIOWrapper: The opened backup file object.
        """
        shutil.copy(BackUpCopies.path_to_original_file, BackUpCopies.backup_file)
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Handles cleanup after exiting the context.

        If no exceptions occurred, deletes the original file.

        Args:
            exc_type: The exception type, if any.
            exc_val: The exception value, if any.
            exc_tb: The traceback object, if any.
        """
        if exc_type is None:
            os.remove(BackUpCopies.path_to_original_file)

        self.file.close()


# Set the paths for the backup functionality
BackUpCopies.set_paths('original_file_task9/text2', 'backup_copies_task9/new_copy')

# Example usage
with BackUpCopies(BackUpCopies.backup_file, 'r') as fr:
    print(fr.readlines())
