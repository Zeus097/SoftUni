from collections import deque


collection = deque(input())
openning_brackets = '{[('
counter = 0

while collection and counter < len(collection) // 2:
    if collection[0] not in openning_brackets:
        break

    if (collection[0] == '{' and collection[1] == '}' or
            collection[0] == '[' and collection[1] == ']' or
            collection[0] == '(' and collection[1] == ')'):
        collection.popleft()
        collection.popleft()
        collection.rotate(counter)
        counter = 0
    else:
        collection.rotate(-1)
        counter += 1

if collection:
    print('NO')
else:
    print('YES')
