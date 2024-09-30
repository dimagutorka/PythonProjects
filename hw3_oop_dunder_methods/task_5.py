class A:


    def __init__(self, list_obj):
        self.list_obj = list_obj
        self.list_sum = 0
        self.list_min = 0

    def __len__(self, arg1):
        return len(arg1)

    def __iter__(self):
        self.n = 0  # we need this so we could iterate our object several time but not only once
        return self

    def __next__(self,arg1):
        if 0 <= self.n < len(self.list_obj):
            result = arg1[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, item, arg1):
        return arg1[item]

    def get_list_sum(self, arg1):
        i = iter(arg1)
        for j in i:
            self.list_sum += j

    def get_list_min(self, arg1):
        i = iter(arg1)
        self.list_min = arg1[0]  # temporary minimal variable
        for j in i:
            if j < self.list_min:
                self.list_min = j


# Create an instance of A

a = A([10, 52, 2, 3, 4, 5])

print(a.get_list_sum(a.list_obj))
print(a.get_list_min(a.list_obj))

print(a.list_min)
print(a.list_sum)



