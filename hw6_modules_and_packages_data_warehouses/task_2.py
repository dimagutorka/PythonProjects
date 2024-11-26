import requests
import json
from typing import Any, Dict


def load_url(url: str) -> Dict[str, Any]:
	"""Loads JSON data from a specified URL.

	Args:
		url (str): The URL to load data from.

	Returns:
		Dict[str, Any]: The JSON data retrieved from the URL.

	Raises:
		Exception: If an error occurs while making the request.
	"""
	try:
		r = requests.get(url, auth=('user', 'pass'))
		r.raise_for_status()  # Raise an error for bad responses
		return r.json()
	except requests.ConnectionError:
		print("Connection error occurred.")
	except requests.HTTPError as e:
		print(f"HTTP error occurred: {e}")
	except json.JSONDecodeError:
		print("Error decoding JSON from the response.")
	except Exception as e:
		print(f"Unexpected error occurred: {e}")
	return {}


def write_json_data_on_file() -> None:
	"""Writes JSON data retrieved from a URL to a local file.

	The data is retrieved from 'https://httpbin.org/get' and written to 'data_warehouses/task_2.json'.
	"""
	json_data = load_url('https://httpbin.org/get')

	if json_data:  # Check if json_data is not empty
		with open('data_warehouses/task_2.json', 'w') as fw:
			json.dump(json_data, fw)
			print("Data written to file successfully.")
	else:
		print("No data to write.")


# Example usage
write_json_data_on_file()
