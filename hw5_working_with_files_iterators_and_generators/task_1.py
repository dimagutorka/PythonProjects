class Iteration:
    """
    A class that provides an iterator over a list of strings.

    Attributes:
        counter (int): Keeps track of the current index for iteration.
        my_list (list[str]): The list of strings to iterate over.

    Methods:
        __len__() -> int: Returns the length of the list.
        __iter__() -> Iteration: Initializes the iterator.
        __next__() -> str: Returns the next item in the list or raises StopIteration.
        __getitem__(item: int) -> str: Retrieves an item from the list at the specified index.
    """

    def __init__(self) -> None:
        self.counter: int = 0
        self.my_list: list[str] = []

    def __len__(self) -> int:
        return len(self.my_list)

    def __iter__(self) -> "Iteration":
        self.counter = len(self.my_list)
        return self

    def __next__(self) -> str:
        self.counter -= 1
        if self.counter >= 0:
            item = self.my_list[self.counter]
            return item
        else:
            raise StopIteration

    def __getitem__(self, item: int) -> str:
        return self.my_list[item]


a = Iteration()

f = open("test", 'r')
a.my_list = f.readlines()

for i in iter(a):
    print(i)
