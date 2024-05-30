from functools import reduce


def operate(operator, *args):
    def add():
        return sum(args)

    def subtract():
        return reduce(lambda x, y: x - y, args)

    def multiply():
        return reduce(lambda x, y: x * y, args if 0 not in args else args)

    def divide():
        return reduce(lambda x, y: x / y, args if 0 not in args else args)

    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
