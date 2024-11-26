import json
from typing import List, Dict

# Define the path to the JSON file
path: str = 'data_warehouses/task_4.json'
# Define a new book to add to the JSON data
new_book: Dict = {
    'title': 'Book 6',
    'Author': 'Author 6',
    'Year of publication': 2020,
    'availability': True
}

json_data_from_file: List[Dict] = []  # Initialize an empty list to hold the JSON data


# Read the existing JSON data from the file
with open(path, 'r') as fr:
    json_data_from_file = json.load(fr)  # Load the JSON data into the list
    json_data_from_file.append(new_book)  # Append the new book to the list

# Write the updated JSON data back to the file
with open(path, 'w') as fw:
    json.dump(json_data_from_file, fw, indent=4)  # Write the updated data to the file with pretty formatting

# Print books that are available
for book in json_data_from_file:
    if book['availability']:
        print(book)
