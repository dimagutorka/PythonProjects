import json

path = 'data_warehouses/task_4.json'
new_book = {'title': 'Book 6', 'Author': 'Author 6', 'Year of publication': 2020, 'availability': True}
json_data_from_file = []


with open(path, 'r') as fr:
	json_data_from_file = json.load(fr)
	json_data_from_file.append(new_book)


with open(path, 'w') as fw:
	json.dump(json_data_from_file, fw)


for i in json_data_from_file:
	if i['availability']:
		print(i)
