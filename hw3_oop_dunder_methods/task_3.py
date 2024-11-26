class Person:
    """A class to represent a person with a name and age."""

    LIST_OF_PEOPLE = []  # Class variable to store a list of all people created

    def __init__(self, name: str, age: int) -> None:
        """Initializes a Person instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age
        Person.LIST_OF_PEOPLE.append(self)  # Add this person to the list of people

    def __lt__(self, other: 'Person') -> bool:
        """Compares two Person objects to check if the current object is younger.

        Args:
            other (Person): The other person to compare with.

        Returns:
            bool: True if the current person's age is less than the other person's age.
        """
        return self.age < other.age

    def __eq__(self, other: 'Person') -> bool:
        """Checks if two Person objects have the same age.

        Args:
            other (Person): The other person to compare with.

        Returns:
            bool: True if both persons have the same age.
        """
        return self.age == other.age

    def __gt__(self, other: 'Person') -> bool:
        """Compares two Person objects to check if the current object is older.

        Args:
            other (Person): The other person to compare with.

        Returns:
            bool: True if the current person's age is greater than the other person's age.
        """
        return self.age > other.age

    @classmethod
    def sorting(cls) -> list:
        """Sorts the list of people by their age.

        Returns:
            list: A sorted list of Person objects by age.
        """
        sorted_people_by_age = sorted(cls.LIST_OF_PEOPLE, key=lambda x: x.age)
        return sorted_people_by_age

# Example usage
p1 = Person('Anton', 33)
p2 = Person('Kirill', 22)
p3 = Person('Nadya', 44)
p4 = Person('Oleg', 11)

# Comparing ages
print(p1 < p2)  # Output: False
print(p1 == p2)  # Output: False
print(p1 > p2)  # Output: True

print(20 * "-")

# Sorting people by age
sorted_people = Person.sorting()

# Printing sorted people
for person in sorted_people:
    print(f"{person.name} and {person.age}")
