class A:

	def __init__(self):
		self.counter = 0
		self.my_list = []

	def __len__(self):
		return len(self.my_list)

	def __iter__(self):
		self.counter = len(self.my_list)
		return self

	def __next__(self):
		self.counter -= 1
		if self.counter >= 0:
			item = self.my_list[self.counter]
			return item
		else:
			raise StopIteration

	def __getitem__(self, item):
		return self.my_list[item]

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		return self


a = A()

f = open("/hw5_working_with_files_iterators_and_generators/test", 'r')
a.my_list = f.readlines()

for i in iter(a):
	print(i)
