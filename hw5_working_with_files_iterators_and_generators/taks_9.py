import shutil
import os


class BackUpCopies:

	path_to_original_file = 'original_file_task9/text2'
	backup_file = 'backup_copies_task9/new_copy'

	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None

	@classmethod
	def set_paths(cls, file_to_backup, destination_directory):
		cls.path_to_original_file = file_to_backup
		cls.backup_file = destination_directory

	def __enter__(self):
		shutil.copy(BackUpCopies.path_to_original_file, BackUpCopies.backup_file)
		self.file = open(self.filename, self.mode)
		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type is None:
			os.remove(BackUpCopies.path_to_original_file)

		self.file.close()


BackUpCopies.set_paths('original_file_task9/text2', 'backup_copies_task9/new_copy')


with BackUpCopies(BackUpCopies.backup_file, 'r') as fr:
	print(fr.readlines())