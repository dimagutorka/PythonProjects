class A:
	def __init__(self, filename):
		self.filename = filename
		self.fileopen = None

	def write1(self, text):
		self.fileopen.write(text + '\n')

	def __enter__(self):
		print("__enter__")
		self.fileopen = open(self.filename, 'w')
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		print("__exit__")
		self.fileopen.close()



with A('text1') as fw:
	print("Main")
	fw.write1('asd')


