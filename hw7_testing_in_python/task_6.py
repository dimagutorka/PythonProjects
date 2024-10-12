class BankAccount:

	def __init__(self, balance):
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def get_balance(self):
		return self.balance

	def __add__(self, other):
		return self + other

	def __sub__(self, other):
		return self - other


