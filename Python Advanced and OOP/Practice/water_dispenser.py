from collections import deque


water_quantity = int(input())
water_line = deque()
name = input()
while name != 'Start':
    water_line.append(name)
    name = input()

command = input()
while command != 'End':
    data = command.split()
    if len(data) == 1:
        liters_to_give = int(data[0])
        person_name = water_line.popleft()
        if liters_to_give <= water_quantity:
            print(f"{person_name} got water")
            water_quantity -= liters_to_give
        else:
            print(f"{person_name} must wait")
    else:
        liters_to_give = int(data[1])
        water_quantity += liters_to_give
    command = input()

print(f"{water_quantity} liters left")
