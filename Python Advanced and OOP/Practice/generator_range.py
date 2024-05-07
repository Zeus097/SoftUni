def genrange(start: int, end: int):
    current = start
    while current <= end:
        yield current
        current += 1


# print(list(genrange(1, 10)))
