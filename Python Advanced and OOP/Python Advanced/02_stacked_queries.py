empty_stack = []
number_of_lines = int(input())
mapper = {
    '1': lambda x: empty_stack.append(int(x)) if x else None,
    '2': lambda: empty_stack.pop() if len(empty_stack) != 0 else None,
    '3': lambda: print(max(empty_stack)) if len(empty_stack) != 0 else None,
    '4': lambda: print(min(empty_stack)) if len(empty_stack) != 0 else None
}

for _ in range(number_of_lines):
    querries = input().split()
    mapper[querries[0]](*querries[1:])

for _ in range(len(empty_stack)):
    print(empty_stack.pop(), end=', ' if len(empty_stack) != 0 else '')
