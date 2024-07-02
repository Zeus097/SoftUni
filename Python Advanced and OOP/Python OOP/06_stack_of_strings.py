from typing import List


class Stack:
    def __init__(self):
        self.data: List = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


# data = Stack()
# print(data.is_empty())
# data.push(5)
# data.push(6)
# print(data.top())
# print(data.is_empty())
# print(data.pop())
# print(data.pop())
# print(data.is_empty())
