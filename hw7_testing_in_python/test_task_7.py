import os
import pytest


@pytest.fixture
def temp_file(tmp_path):
	temp_dir = tmp_path / "my_temp_dir"
	temp_dir.mkdir()
	temp_file = temp_dir / "test_file.txt"

	return temp_file


def test_create_write_in_file(temp_file):
	temp_file.write_text("Hello, pytest!")
	size_of_the_file_in_mbytes = os.path.getsize(temp_file) / 1024 / 1024

	assert temp_file.is_file()
	assert temp_file.read_text() == "Hello, pytest!"
	assert size_of_the_file_in_mbytes < 3


def test_read_file(temp_file):
	temp_file.write_text("Hello, pytest!")

	assert temp_file.read_text() != ' '

	try:
		assert temp_file.is_file()
	except Exception as e:
		raise e


