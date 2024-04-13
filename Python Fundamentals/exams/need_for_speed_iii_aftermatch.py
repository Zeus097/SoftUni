def car_collection(cars_number):
    collection = {}
    for index in range(cars_number):
        current_car = input().split('|')
        car_name = current_car[0]
        car_mileage = current_car[1]
        car_fuel = current_car[2]
        collection[car_name] = {'MILEAGE': int(car_mileage), 'FUEL': int(car_fuel)}

    return collection


def game(cars):
    while True:
        command = input()
        if command == 'Stop':
            break

        action = command.split(' : ')
        if action[0] == 'Drive':
            car_type = action[1]
            distance = int(action[2])
            fuel_liters = int(action[3])
            if cars[car_type]['FUEL'] >= fuel_liters:
                cars[car_type]['MILEAGE'] += distance
                cars[car_type]['FUEL'] -= fuel_liters
                print(f"{car_type} driven for {distance} kilometers. {fuel_liters} liters of fuel consumed.")
                if cars[car_type]['MILEAGE'] >= 100000:
                    del cars[car_type]
                    print(f"Time to sell the {car_type}!")
            else:
                print("Not enough fuel to make that ride")

        elif action[0] == 'Refuel':
            current_car = action[1]
            liters = int(action[2])
            refiled_liters = 0
            if cars[current_car]['FUEL'] + liters <= 75:
                cars[current_car]['FUEL'] += liters
                refiled_liters += liters
            else:
                refiled_liters = 75 - cars[current_car]['FUEL']
                cars[current_car]['FUEL'] = 75
            print(f"{current_car} refueled with {refiled_liters} liters")

        elif action[0] == 'Revert':
            selected_car = action[1]
            kilometers = int(action[2])
            cars[selected_car]['MILEAGE'] -= kilometers
            if cars[selected_car]['MILEAGE'] >= 10000:
                print(f"{selected_car} mileage decreased by {kilometers} kilometers")
            else:
                cars[selected_car]['MILEAGE'] = 10000

    for car in cars:
        mileage = cars[car]['MILEAGE']
        fuel = cars[car]['FUEL']
        print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


number_of_obtained_cars = int(input())
owned_cars = car_collection(number_of_obtained_cars)
game(owned_cars)
