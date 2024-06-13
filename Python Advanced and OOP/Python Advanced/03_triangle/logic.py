def upper_part(n):
    for i in range(n):
        for j in range(1, n + i - (n // 2)):
            print(j, end=' ')
        print()


def lower_part(n):
    for i in range(n):
        for j in range(1, n - i):
            print(j, end=' ')
        print()


