import json
import xmltodict
import csv
from typing import List, Dict, Any


class XmlToJson:
    """A context manager class for converting XML data to JSON."""

    json_data: str = ""

    def __init__(self, filename: str, mode: str) -> None:
        """Initializes the XmlToJson with the specified filename and mode.

        Args:
            filename (str): The name of the XML file to read from or write to.
            mode (str): The mode for opening the file ('r' for reading, 'w' for writing).
        """
        self.filename = filename
        self.mode = mode

    def __enter__(self) -> 'XmlToJson':
        """Opens the specified file and returns the instance."""
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Closes the file when exiting the context."""
        self.file.close()

# Convert XML to JSON
with XmlToJson('data_warehouses/task_6.xml', 'r') as xml_file:
    data_dict = xmltodict.parse(xml_file.file.read())
    XmlToJson.json_data = json.dumps(data_dict)

# Write JSON data to a file
with open('data_warehouses/task_6.json', 'w') as json_file:
    json_file.write(XmlToJson.json_data)


class CsvToJson:
    """A context manager class for converting CSV data to JSON and vice versa."""

    json_data_from_csv: List[Dict[str, Any]] = []
    csv_data_from_json: Dict[str, Any] = {}

    def __init__(self, filename: str, mode: str) -> None:
        """Initializes the CsvToJson with the specified filename and mode.

        Args:
            filename (str): The name of the CSV file to read from or write to.
            mode (str): The mode for opening the file ('r' for reading, 'w' for writing).
        """
        self.filename = filename
        self.mode = mode

    def __enter__(self) -> 'CsvToJson':
        """Opens the specified file and returns the instance."""
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Closes the file when exiting the context."""
        self.file.close()


# Convert CSV to JSON
with CsvToJson('data_warehouses/task_csv_to_json.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file.file)
    for row in csv_reader:
        CsvToJson.json_data_from_csv.append(row)

# Write JSON data to a file
with open('data_warehouses/task_6_json_to_csv.json', 'w') as json_file:
    json.dump(CsvToJson.json_data_from_csv, json_file)

# Convert JSON back to CSV
with open('data_warehouses/taks_6_from_json_to_csv.csv', 'w', newline='') as csv_file:
    headers = CsvToJson.json_data_from_csv[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(CsvToJson.json_data_from_csv)
