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
