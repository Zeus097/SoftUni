from collections import deque


first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = deque(input().split())
    if command[0] == 'Add':
        command.popleft()
        if command[0] == 'First':
            command.popleft()
            for num in command:
                first_sequence.add(int(num))

        elif command[0] == 'Second':
            command.popleft()
            for num in command:
                second_sequence.add(int(num))

    elif command[0] == 'Remove':
        command.popleft()
        if command[0] == 'First':
            command.popleft()
            for num in command:
                if int(num) in first_sequence:
                    first_sequence.remove(int(num))
        elif command[0] == 'Second':
            command.popleft()
            for num in command:
                if int(num) in second_sequence:
                    second_sequence.remove(int(num))

    elif command[0] == 'Check' and command[1] == 'Subset':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print(True)
        else:
            print(False)

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
