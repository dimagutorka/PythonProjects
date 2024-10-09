def even_number_generator() -> int:
    """A generator that yields even numbers starting from 0.

    Yields:
        int: The next even number in the sequence.
    """
    number = 0
    while True:
        yield number
        number += 2


file_name = 'limited_generator/even_numbers_from_generator'


def write_even_numbers_to_file(path: str, limit: int = 100) -> None:
    """Writes even numbers to a specified file up to a given limit.

    Args:
        path (str): The path to the file where even numbers will be written.
        limit (int, optional): The number of even numbers to write. Defaults to 100.
    """
    gen = even_number_generator()

    with open(path, 'w') as fw:
        for _ in range(limit):
            fw.write(f'{next(gen)}\n')

# Example usage
write_even_numbers_to_file(file_name, 100)
