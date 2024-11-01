from datetime import datetime  # Module for working with date and time objects


def reformat_date(date: str) -> None:
	"""
	Reformats a date from 'dd/mm/yyyy' format to 'yyyy/mm/dd' format.

	Parameters:
	date (str): The input date as a string in 'dd/mm/yyyy' format.

	Returns:
	None: Prints the reformatted date or an error message if the format is incorrect.
	"""
	try:
		# Parse the input date string into a datetime object using the specified format
		initial_date = datetime.strptime(date, '%d/%m/%Y')

		# Format the datetime object into 'yyyy/mm/dd' format
		reformated_date = initial_date.strftime("%Y/%m/%d")

		# Print the reformatted date
		print(f'Reformatted date: {reformated_date}')
	except ValueError:
		# Handle the case where the input date format is incorrect
		print('Your date is in the wrong format')
