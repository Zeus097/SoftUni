def cities_info():
    collection = {}
    while True:
        string_with_cities = input()
        if string_with_cities == 'Sail':
            break

        command_line = string_with_cities.split('||')
        city = command_line[0]
        population = int(command_line[1])
        gold = int(command_line[2])
        if city not in collection:
            collection[city] = {'POPULATION': population, 'GOLD': gold}
        else:
            collection[city]['POPULATION'] += population
            collection[city]['GOLD'] += gold

    return collection


def plunder(target_city_collection):
    while True:
        command = input()
        if command == 'End':
            break

        action = command.split('=>')
        if action[0] == 'Plunder':
            current_city = action[1]
            current_people = int(action[2])
            current_gold = int(action[3])
            target_city_collection[current_city]['POPULATION'] -= current_people
            target_city_collection[current_city]['GOLD'] -= current_gold
            print(f"{current_city} plundered! {current_gold} gold stolen, {current_people} citizens killed.")
            if (target_city_collection[current_city]['POPULATION'] <= 0 or
                    target_city_collection[current_city]['GOLD'] <= 0):
                del target_city_collection[current_city]
                print(f"{current_city} has been wiped off the map!")

        elif action[0] == 'Prosper':
            town = action[1]
            town_gold = int(action[2])
            if town_gold < 0:
                print("Gold added cannot be a negative number!")
                continue
            else:
                target_city_collection[town]['GOLD'] += town_gold
                print(f"{town_gold} gold added to the city treasury. "
                      f"{town} now has {target_city_collection[town]['GOLD']} gold.")

    if len(target_city_collection) != 0:
        count = len(target_city_collection)
        print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
        for city in target_city_collection:
            people = target_city_collection[city]['POPULATION']
            gold = target_city_collection[city]['GOLD']
            print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


city_collection = cities_info()
plunder(city_collection)
