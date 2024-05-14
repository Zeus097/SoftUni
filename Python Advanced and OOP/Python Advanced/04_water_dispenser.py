from collections import deque


starting_quantity = int(input())
queue = deque()
name = input()

while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    if command.isdigit():
        litters = int(command)
        person_name = queue.popleft()
        if litters <= starting_quantity:
            print(f"{person_name} got water")
            starting_quantity -= litters
        else:
            print(f"{person_name} must wait")
    else:
        command_name, litters = command.split()
        starting_quantity += int(litters)

    command = input()

print(f"{starting_quantity} liters left")
