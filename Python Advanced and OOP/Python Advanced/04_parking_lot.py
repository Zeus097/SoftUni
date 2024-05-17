commands_number = int(input())
parking_lot = set()

for _ in range(commands_number):
    command_line = input().split(', ')
    direction, car_number = command_line[0], command_line[1]

    if direction == 'IN':
        parking_lot.add(car_number)
    elif direction == 'OUT':
        parking_lot.remove(car_number)

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print("Parking Lot is Empty")
