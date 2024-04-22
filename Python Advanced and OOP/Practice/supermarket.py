from collections import deque


customer_line = deque()
name = input()
while name != 'End':
    if name == 'Paid':
        while customer_line:
            print(customer_line.popleft())
    else:
        customer_line.append(name)

    name = input()
print(f"{len(customer_line)} people remaining.")
