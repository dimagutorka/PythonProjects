def create_class(class_name: str, methods: dict) -> type:
	"""Creates a new class dynamically using the provided methods.

    Args:
        class_name (str): The name of the class to create.
        methods (dict): A dictionary of method names and their corresponding function implementations.

    Returns:
        type: The newly created class.
    """
	# Create a class using type, with no base classes (hence the empty tuple)
	return type(class_name, (object,), methods)


def constructor(self: object, name: str, age: int) -> None:
	"""Initializes the object with name and age attributes.

    Args:
        self (object): The instance of the class.
        name (str): The name of the individual.
        age (int): The age of the individual.
    """
	self.name = name
	self.age = age


def say_hello(self: object, arg: str) -> str:
	return "Hello " + arg


def say_goodbye(self: object) -> str:
	return "Goodbye!"


# Dictionary of methods to be included in the new class
methods = {
	"say_hello": say_hello,
	"say_goodbye": say_goodbye,
	"__init__": constructor
}

# Create a class named 'Geeks' with the methods provided in the dictionary
Geeks = create_class("Geeks", methods)

# Instantiate the class
obj = Geeks("dima", 123)

# Display the object's attributes and call its methods
print(obj.__dict__)
