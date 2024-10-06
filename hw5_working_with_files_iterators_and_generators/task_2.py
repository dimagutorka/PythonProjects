import uuid

list_if_uuid = []


def uuid_generator(number_of_uuid):
	for i in range(number_of_uuid):
		list_if_uuid.append(uuid.uuid4())


uuid_generator(10)

iterable_object = iter(list_if_uuid)

print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
