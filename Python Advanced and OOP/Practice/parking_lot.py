commands_number = int(input())
cars = set()

for _ in range(commands_number):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        cars.add(car_number)
    elif direction == 'OUT':
        cars.remove(car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
