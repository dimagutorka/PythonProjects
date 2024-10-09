import json

class Configuration:
    """A context manager for reading and writing JSON configuration files.

    Attributes:
        json_data (dict): The JSON data loaded from the file.
        filename (str): The name of the file to read from or write to.
        mode (str): The mode for opening the file ('r' for reading, 'w' for writing).
        file (TextIOWrapper): The file object for reading or writing.
    """

    json_data: dict = None

    def __init__(self, filename: str, mode: str) -> None:
        """Initializes the Configuration object.

        Args:
            filename (str): The name of the JSON file to operate on.
            mode (str): The mode for opening the file ('r' or 'w').
        """
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> 'TextIOWrapper':
        """Opens the file and loads JSON data if in read mode.

        Returns:
            TextIOWrapper: The opened file object.
        """
        self.file = open(self.filename, self.mode)

        if self.mode == 'r':
            Configuration.json_data = json.load(self.file)
            print(f'Reading file... \n{Configuration.json_data}')

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Closes the file when exiting the context.

        Args:
            exc_type: The exception type, if any.
            exc_val: The exception value, if any.
            exc_tb: The traceback object, if any.
        """
        self.file.close()

# Example usage: Modifying JSON configuration
with Configuration('json_files_task8/config.json', 'r') as fr:
    Configuration.json_data["a"] = 30
    Configuration.json_data["b"] = 40
    Configuration.json_data["c"] = 50

with Configuration('json_files_task8/config.json', 'w') as fw:
    json.dump(Configuration.json_data, fw)
