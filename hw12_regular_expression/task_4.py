import re
from datetime import datetime


def reformat_date(date):
	try:
		initial_date = datetime.strptime(date, '%d/%m/%Y')
		reformated_date = initial_date.strftime("%Y/%m/%d")
		return print(f'Reformat date: {reformated_date}')
	except ValueError:
		print('Your date is in wrong format')