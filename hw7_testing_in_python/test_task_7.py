import pytest


@pytest.fixture
def temp_file(tmp_path):
	"""
	Fixture to create a temporary file in a temporary directory.
	"""
	temp_dir = tmp_path / "my_temp_dir"
	temp_dir.mkdir()
	temp_file = temp_dir / "test_file.txt"
	return temp_file


def test_create_write_in_file(temp_file):
	"""
	Test that a file can be created, written to, and checked for size.
	"""
	# Write content to the temporary file
	temp_file.write_text("Hello, pytest!")

	# Check if the file was created and contains the correct content
	assert temp_file.is_file(), "The file should exist."
	assert temp_file.read_text() == "Hello, pytest!", "The file content does not match."

	# Check file size is less than 3 MB
	file_size_mb = temp_file.stat().st_size / (1024 * 1024)
	assert file_size_mb < 3, "The file size should be less than 3 MB."


def test_read_file(temp_file):
	"""
	Test that a file can be read and is not empty.
	"""
	# Write content to the temporary file
	temp_file.write_text("Hello, pytest!")

	# Verify file content is not empty and file exists
	assert temp_file.read_text() != ' ', "The file should not be empty."
	assert temp_file.is_file(), "The file should exist."
