class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while self.start_index > 0:
            self.start_index -= 1
            return self.iterable[self.start_index]
        raise StopIteration


# Test code

# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
