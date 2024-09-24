"""TASK 1"""
"NOTE: I wasn't sure what solution is considered to be correct, so I coded 2 options I could come up with"

text = "This is my custom sum function!"
list_number = [1, 2, 3, 4, 5]

"SOLUTION 1"


def my_sum1():
	global sum

	def sum(*args):
		print(text)


print(sum(list_number))
my_sum1()
sum()

"SOLUTION 2"


def my_sum2():
	def sum(*args):
		print(text)

	return sum


print(sum(list_number))
sum = my_sum2()
sum(text)

"""TASK 2"""
subscribers = []


def subscribe(sub_name):
	subscribers.append(sub_name)

	def confirm_subscription():
		print(f"The subscription for {sub_name} is confirmed ")

	confirm_subscription()


def unsubscribe(sub_name):
	if sub_name in subscribers:
		subscribers.remove(sub_name)
		print(f"{sub_name} is unsubscribed successfully ")
	else:
		print(f"{sub_name} is not found in the subscription list")


subscribe("Dima")
subscribe("Nadya")
print(subscribers)
unsubscribe("Dima")
unsubscribe("Anton")
print(subscribers)

"""TASK 3"""
discount = 0.1


def create_order(goods_price):
	final_price = goods_price - goods_price * discount

	def apply_additional_discount():
		nonlocal final_price
		final_price -= final_price * discount

		print(f"Your final price is {final_price}")

	return apply_additional_discount


order_creation_plus_discount = create_order(100)
order_creation_plus_discount()

"""TASK 4"""

default_time = 60


def training_session(num_rounds):
	time_per_round = default_time

	def adjust_time(new_time):
		nonlocal time_per_round
		time_per_round = new_time

	for round_num in range(1, num_rounds + 1):
		if round_num % 2 != 0:
			new_time = int(input(f"Enter the time for round {round_num} (minutes): "))
			adjust_time(new_time)

		print(f"Round {round_num}: {time_per_round} minutes")


num_rounds = int(input("Enter the number of training rounds: "))
training_session(num_rounds)



"""TASK 5"""

events = [1, 2, 3]


def calendar():
	def inner(action="show", event=None):
		if action == "show":
			print(events)
		elif action == "del":
			events.remove(event)
		else:
			events.append(event)
		return events

	return inner


add_event = calendar()
del_event = calendar()
show_events = calendar()

show_events()
add_event("add", 4)
show_events()
del_event("del", 1)
show_events()

"""TASK 6"""


def create_calculator(action):
	if action == "+":
		def addition(number_1, number_2):
			return number_1 + number_2

		return addition

	elif action == "-":
		def subtraction(number_1, number_2):
			return number_1 - number_2

		return subtraction

	elif action == "/":
		def division(number_1, number_2):
			return number_1 / number_2

		return division

	else:
		def multiplication(number_1, number_2):
			return number_1 * number_2

		return multiplication


subtraction = create_calculator("-")
print(subtraction(10, 5))  # 5

addition = create_calculator("+")
print(addition(10, 5))  # 15

division = create_calculator("/")
print(division(10, 5))  # 2.0

multiplication = create_calculator("*")
print(multiplication(10, 5))  # 50

"""TASK 7"""

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

"""TASK 8"""


def create_user_settings():

	settings = {
		'theme': 'default',
		'language': 'en',
		'notifications': True
	}

	def manage_settings(setting_name=None, value=None):
		if setting_name is None:
			return settings
		elif value is None:
			return settings.get(setting_name, 'Setting not found')
		else:
			settings[setting_name] = value
			return f"Setting '{setting_name}' updated to '{value}'"

	return manage_settings


user_settings = create_user_settings()
print(user_settings())
print(user_settings('theme'))
print(user_settings('theme', 'Christmas'))
print(user_settings('language', 'zh'))
print(user_settings('theme'))
print(user_settings())


"""TASK 9"""

def get_factorial(n):
	if n == 0:
		return 1
	return n * get_factorial(n-1)


def memoize(func):
	cache = {

	}

	def inner(n):
		if n in cache:
			print(f"Factorial {n} is already calculated and can be retrieved from cache")
			return cache[n]
		print(f"Factorial {n} is new and has to be calculated")
		result = func(n)
		cache[n] = result
		return result

	return inner


a = memoize(get_factorial)
print(a(4))
print(a(4))



"""TASK 10"""


def create_product(name, amount, price):

	product_data = {"Name": name,
	                "Amount": amount,
	                "Price": price
	                }

	def price_change(new_price):
		product_data["Price"] = new_price

		return product_data

	return price_change


a = create_product("Name", 22, 110)
print(a(11))
