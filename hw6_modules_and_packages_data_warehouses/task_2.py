import requests
import json


def load_url(url):
	try:
		r = requests.get(url, auth=('user', 'pass'))
		return r.json()
	except ConnectionError:
		print(f"Unexpected error occurred")


def write_json_data_on_file():
	with open('data_warehouses/task_2.json', 'w') as fw:
		json_data = load_url('https://httpbin.org/get')
		json.dump(json_data, fw)


write_json_data_on_file()