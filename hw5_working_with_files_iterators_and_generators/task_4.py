path_to_big_file = 'images_and_files/big_file'
path_to_filtered_file = 'images_and_files/only_lines_with_keyword'


def generator_of_lines_fromfile() -> str:
    """Generator function that yields lines from a specified file.

    Yields:
        str: The next line from the file.
    """
    with open(path_to_big_file, 'r') as fr:
        yield from fr.readlines()


def write_lines_by_keyword_infile(key_word: str) -> None:
    """Writes lines from the big file to a new file if they contain the specified keyword.

    Args:
        key_word (str): The keyword to search for in the lines of the file.
    """
    gen = generator_of_lines_fromfile()
    with open(path_to_filtered_file, 'w') as fw:
        for line in gen:
            if key_word in line:
                fw.write(line)

# Example usage
write_lines_by_keyword_infile('How')
