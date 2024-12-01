class DynamicProperties:
    """A class that allows dynamic addition of properties using getter and setter methods."""

    def __init__(self) -> None:
        """Initializes an empty dictionary to store property values."""
        self._properties = {}

    def add_property(self, name: str) -> None:
        """Adds a property with the specified name.

        Args:
            name (str): The name of the property to add.
        """
        def getter(self) -> any:
            """Getter for the dynamic property."""
            return self._properties.get(name, None)

        def setter(self, value: any) -> None:
            """Setter for the dynamic property.

            Args:
                value (any): The value to set for the property.
            """
            self._properties[name] = value

        # Create property using the built-in property function
        setattr(self.__class__, name, property(getter, setter))


# Example usage
dynamic_obj = DynamicProperties()
dynamic_obj.add_property('example_property')

# Set the property
dynamic_obj.example_property = 'Hello, World!'

# Get the property
result = dynamic_obj.example_property
print(result)  # Output: Hello, World!
