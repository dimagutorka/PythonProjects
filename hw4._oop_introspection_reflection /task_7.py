import functools

# Decorator to log a method's name and arguments
def log_method_call(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        # Log method name and arguments
        print(f"Calling method: {method.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = method(*args, **kwargs)
        print(f"Method {method.__name__} returned: {result}")
        return result
    return wrapper

# Class decorator to log all methods
def log_methods(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):  # Check if the attribute is callable (i.e., it's a method)
            setattr(cls, attr_name, log_method_call(attr_value))
    return cls

# Example class using log_methods decorator
@log_methods
class MyClass:
    def method_one(self, x):
        return x * 2

    def method_two(self, y, z):
        return y + z

# Example usage
obj = MyClass()
obj.method_one(5)
obj.method_two(3, 7)
