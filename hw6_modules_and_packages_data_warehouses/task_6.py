import json
import xmltodict
import csv


class XmlToJson:

	json_data = {}

	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode

	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		return self


with XmlToJson('data_warehouses/task_6.xml', 'r') as fr:
	data_dict = xmltodict.parse(fr.read())
	XmlToJson.json_data = json.dumps(data_dict)


with XmlToJson('data_warehouses/task_6.json', 'w') as fw:
	json.dump(XmlToJson.json_data, fw)


class CsvToJson:

	json_data_from_csv = []
	csv_data_from_json = {}

	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode

	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		return self


with CsvToJson('data_warehouses/task_csv_to_json.csv', 'r') as fr:
	csvReader = csv.DictReader(fr)
	id = 1

	for rows in csvReader:
		CsvToJson.json_data_from_csv.append(rows)

with CsvToJson('data_warehouses/task_6_json_to_csv.json', 'w') as fw:
	json.dump(CsvToJson.json_data_from_csv, fw)


with CsvToJson('data_warehouses/taks_6_from_json_to_csv.csv', 'w') as fw:
	headers = CsvToJson.json_data_from_csv[0].keys()

	writer = csv.DictWriter(fw, fieldnames=headers)
	writer.writeheader()
	writer.writerows(CsvToJson.json_data_from_csv)







