total_expense = 0


def add_expenses(expenses):
	global total_expense
	total_expense += expenses
	return total_expense


def get_expense():
	return total_expense


user_choice = input("Type 1 to add expenses \nType 0 to get expenses \n")

if user_choice == '1':
	print(add_expenses(int(input("Enter the expenses you want to add\n"))))
else:
	print(get_expense())
