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