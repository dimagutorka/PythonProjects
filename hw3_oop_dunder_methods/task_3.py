class Person:

	LIST_OF_PEOPLE = []

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.LIST_OF_PEOPLE.append(self)

	def __lt__(self, other):
		return self.age < other.age

	def __eq__(self, other):
		return self.age == other.age

	def __gt__(self, other):
		return self.age > other.age

	@classmethod
	def sorting(cls):
		sorted_people_by_age = sorted(cls.LIST_OF_PEOPLE, key=lambda x: x.age)
		return sorted_people_by_age


p1 = Person('Anton', 33)
p2 = Person('Kirill', 22)
p3 = Person('Nadya', 44)
p4 = Person('Oleg', 11)

print(p1 < p2)
print(p1 == p2)
print(p1 > p2)

print(20 * "-")  # utility print for better readability

sorted_people = Person.sorting()

for i in sorted_people:
	print(f"{i.name} and {i.age}")
