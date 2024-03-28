obtained_cars = int(input())
car = {}

for _ in range(obtained_cars):
    car_info = input().split("|")
    car_name = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    car[car_name] = {'MILEAGE': mileage, 'FUEL': fuel}

while True:
    command = input()
    if command == "Stop":
        break

    action = command.split(" : ")

    if action[0] == "Drive":
        current_car = action[1]
        distance = int(action[2])
        current_fuel = int(action[3])
        if car[current_car]['FUEL'] < current_fuel:
            print("Not enough fuel to make that ride")
        else:
            car[current_car]['MILEAGE'] += distance
            car[current_car]['FUEL'] -= current_fuel
            print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")

        if car[current_car]['MILEAGE'] >= 100000:
            del car[current_car]
            print(f"Time to sell the {current_car}!")

    elif action[0] == "Refuel":
        current_car = action[1]
        current_fuel = int(action[2])
        needed_fuel = 0
        car[current_car]['FUEL'] += current_fuel
        if car[current_car]['FUEL'] > 75:
            needed_fuel += (75 + current_fuel) - (car[current_car]['FUEL'])
            car[current_car]['FUEL'] = 75
        else:
            needed_fuel = current_fuel

        print(f"{current_car} refueled with {needed_fuel} liters")

    elif action[0] == "Revert":
        current_car = action[1]
        current_kilometers = int(action[2])
        car[current_car]['MILEAGE'] -= current_kilometers

        if car[current_car]['MILEAGE'] < 10000:
            car[current_car]['MILEAGE'] = 10000
        else:
            print(f"{current_car} mileage decreased by {current_kilometers} kilometers")

for key, value in car.items():
    car_left = key
    mileage_left = car[car_left]['MILEAGE']
    fuel_left = car[car_left]['FUEL']

    print(f"{car_left} -> Mileage: {mileage_left} kms, Fuel in the tank: {fuel_left} lt.")
