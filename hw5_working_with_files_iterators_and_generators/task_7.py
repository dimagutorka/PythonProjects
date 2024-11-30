path_to_log = 'log_files/log_file.log'
path_to_errors = 'log_files/errors_only'


def generator(path_log_file: str) -> str:
    """A generator function that yields lines from a specified log file.

    Args:
        path_log_file (str): The path to the log file to read from.

    Yields:
        str: The next line from the log file.
    """
    with open(path_log_file, 'r') as fr:
        yield from fr.readlines()


def error_filter(path_to_error_file: str) -> None:
    """Filters error lines from the log file and writes them to a new file.

    Args:
        path_to_error_file (str): The path to the file where error lines will be written.
    """
    gen = generator(path_to_log)
    with open(path_to_error_file, 'w') as fw:
        for line in gen:
            if 'error' in line.lower():  # Convert to lower case for case-insensitive matching
                fw.write(line)


# Example usage
error_filter(path_to_errors)
