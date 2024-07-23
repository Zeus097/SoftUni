def read_next(*iterables):
    for iterable in iterables:
        # for element in iterable:
        #     yield element

        yield from iterable


# # Test code
#
# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')
