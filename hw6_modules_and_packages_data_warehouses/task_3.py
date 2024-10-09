import csv
from typing import List, Dict

filename = '/Users/cblpok/Documents/GitHub/PythonProjects/hw6_modules_and_packages_data_warehouses/data_warehouses/task_3.csv'

fields = ['name', 'age', 'mark']

my_dict = [
    {'name': 'kirill', 'age': '32', 'mark': '45'},
    {'name': 'ruslana', 'age': '35', 'mark': '32'},
    {'name': 'katya', 'age': '22', 'mark': '12'}
]

data_from_csv: List[Dict[str, str]] = []  # Initialize an empty list to store data read from CSV


def read_csv(path: str) -> None:
    """Reads a CSV file and appends its contents to the data_from_csv list.

    Args:
        path (str): The path to the CSV file to read.
    """
    with open(path, 'r') as fr:
        csvreader = csv.DictReader(fr)

        for row in csvreader:
            dicts_without_spaces = {key.strip(): value.strip() for key, value in row.items()}
            data_from_csv.append(dicts_without_spaces)
            print(dicts_without_spaces)


def add_student_to_csv(path: str) -> None:
    """Appends a list of students to the specified CSV file.

    Args:
        path (str): The path to the CSV file where data will be appended.
    """
    with open(path, 'a+', newline='') as fw:  # newline='' to prevent blank lines in some platforms
        writer = csv.DictWriter(fw, fieldnames=fields)
        writer.writerows(my_dict)


def average_mark() -> float:
    """Calculates the average mark from the data read from the CSV file.

    Returns:
        float: The average mark of all students.
    """
    if not data_from_csv:  # Check if there are any records
        return 0.0

    total_marks = sum(int(data['mark']) for data in data_from_csv)
    return total_marks / len(data_from_csv)  # Return average


# Example usage
read_csv(filename)
add_student_to_csv(filename)
print(f"Average Mark: {average_mark():.2f}")
