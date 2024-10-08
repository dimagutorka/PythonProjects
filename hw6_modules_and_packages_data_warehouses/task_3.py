import csv

filename = '/Users/cblpok/Documents/GitHub/PythonProjects/hw6_modules_and_packages_data_warehouses/data_warehouses/task_3.csv'

fields = ['name', 'age', 'mark']

my_dict = [{'name': 'kirill', 'age': '32', 'mark': '45'},
           {'name': 'ruslana', 'age': '35', 'mark': '32'},
           {'name': 'katya', 'age': '22', 'mark': '12'}
           ]

data_from_csv = []


def read_csv(path):
	with open(path, 'r') as fr:
		csvreader = csv.DictReader(fr)

		for row in csvreader:
			dicts_without_spaces = {key.strip(): value.strip() for key, value in row.items()}
			data_from_csv.append(dicts_without_spaces)
			print(dicts_without_spaces)


read_csv(filename)


def add_student_to_csv(path):
	with open(path, 'a+') as fw:
		writer = csv.DictWriter(fw, fieldnames=fields)
		writer.writerows(my_dict)


add_student_to_csv(filename)


def average_mark():
	avg_mark = 0
	for data in data_from_csv:
		avg_mark += int(data['mark'])
	return avg_mark


print(average_mark())

