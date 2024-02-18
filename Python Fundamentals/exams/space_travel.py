travel_route = input().split("||")

start_amount_of_fuel = int(input())
start_amount_of_ammunition = int(input())


while True:

    if travel_route[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    command = travel_route.pop(0)
    current_command = command.split(" ")

    if current_command[0] == "Travel":
        given_distance = int(current_command[1])
        start_amount_of_fuel -= given_distance
        if start_amount_of_fuel >= 0:
            print(f"The spaceship travelled {given_distance} light-years.")
        else:
            print("Mission failed.")
            break

    elif current_command[0] == "Enemy":
        enemy_armour = int(current_command[1])
        if start_amount_of_ammunition >= enemy_armour:
            start_amount_of_ammunition -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        else:
            start_amount_of_fuel -= enemy_armour * 2
            if start_amount_of_fuel >= 0:
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif current_command[0] == "Repair":
        given_resources = int(current_command[1])
        start_amount_of_fuel += given_resources
        start_amount_of_ammunition += given_resources * 2
        ammunition_add = given_resources *2
        fuel_add = given_resources
        print(f"Ammunitions added: {ammunition_add}.")
        print(f"Fuel added: {fuel_add}.")

