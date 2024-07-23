class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= self.count:
            return self.count - self.i
        raise StopIteration


# # Test code
#
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")

# # Test code 2
#
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")
