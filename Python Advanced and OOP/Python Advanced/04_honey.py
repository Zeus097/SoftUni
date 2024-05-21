from collections import deque


bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
making_process = deque([x for x in input().split()])

honey = 0
matched_bee = deque([])
matched_nectar = deque([])


mapper = {"+": lambda x, y: x + y,
          "-": lambda x, y: x - y,
          "*": lambda x, y: x * y,
          "/": lambda x, y: x / y if y != 0 else 0
          }

while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey += abs(mapper[making_process[0]](bees[0], nectar[-1]))
        nectar.pop()
        bees.popleft()
        making_process.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
