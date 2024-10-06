import json


class Configuration:

	json_data = None

	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None

	def __enter__(self):
		self.file = open(self.filename, self.mode)

		if self.mode == 'r':
			Configuration.json_data = json.load(self.file)
			print(f'Reading file... \n{Configuration.json_data}')

		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.file.close()


with Configuration('json_files_task8/config.json', 'r') as fr:
	Configuration.json_data["a"] = 30
	Configuration.json_data["b"] = 40
	Configuration.json_data["c"] = 50


with Configuration('json_files_task8/config.json', 'w') as fw:
	json.dump(Configuration.json_data, fw)






