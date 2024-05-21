from collections import deque
from functools import reduce


def add(numbers):
    expression.appendleft(str(reduce(lambda a, b: a + b, numbers)))


def subtract(numbers):
    expression.appendleft(str(reduce(lambda a, b: a - b, numbers)))


def multiply(numbers):
    expression.appendleft(str(reduce(lambda a, b: a * b, numbers)))


def divide(numbers):
    expression.appendleft(str(reduce(lambda a, b: a // b, numbers)))


expression = deque(input().split())
nums = []
operators = "*/+-"

while True:
    character = expression.popleft()
    if character not in operators:
        nums.append(int(character))
    else:
        if character == "*":
            multiply(nums)
        elif character == "/":
            divide(nums)
        elif character == "+":
            add(nums)
        elif character == "-":
            subtract(nums)

        nums.clear()
        if len(expression) == 1:
            break


print(*expression)
