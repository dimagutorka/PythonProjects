class SingletonMeta(type):
	_instances = {}
	_rotation = {}

	def __call__(cls, *args, **kwargs):
		# Check if there is an existing instance for the class
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = [instance]
			cls._rotation[cls] = 0
		else:
			# Rotate through the instances
			cls._rotation[cls] = (cls._rotation[cls] + 1) % len(cls._instances[cls])

		# Return the current rotated instance
		return cls._instances[cls][cls._rotation[cls]]

	def create_instance(cls, *args, **kwargs):
		# Allow explicit creation of a new instance and add it to the rotation
		instance = super().__call__(*args, **kwargs)
		cls._instances[cls].append(instance)
		return instance


# Example class using SingletonMeta
class MyClass(metaclass=SingletonMeta):
	def __init__(self, value):
		self.value = value

	def display(self):
		print(f"MyClass instance with value: {self.value}")


# Example usage
# First call creates an instance
a = MyClass(1)
a.display()

# Second call rotates back to the same instance (since it's the only one)
b = MyClass(2)
b.display()

# Create a new instance explicitly
c = MyClass.create_instance(3)
c.display()

# Now it will rotate between the instances
d = MyClass(4)
d.display()

# Output should rotate through the values as per instance creation
