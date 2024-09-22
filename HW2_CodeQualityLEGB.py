"""TASK 1"""
"NOTE: I'm not sure what solution is considered to be correct, so I coded 2 options I could come up with"

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
