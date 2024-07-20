class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.index = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        while self.index <= self.end:
            return self.index
        raise StopIteration


# Test code

# one_to_ten = custom_range(5, 12)
# for num in one_to_ten:
#     print(num)
