city_targets = {}
while True:
    command = input()
    if command == 'Sail':
        break

    city, population, gold = command.split('||')
    if city not in city_targets:
        city_targets[city] = {'POPULATION': int(population), 'GOLD': int(gold)}
    else:
        city_targets[city]['POPULATION'] += int(population)
        city_targets[city]['GOLD'] += int(gold)

while True:
    second_command = input()
    if second_command == 'End':
        break

    action = second_command.split('=>')
    if action[0] == 'Plunder':
        current_town = action[1]
        current_people = int(action[2])
        current_gold = int(action[3])
        city_targets[current_town]['POPULATION'] -= current_people
        city_targets[current_town]['GOLD'] -= current_gold
        print(f"{current_town} plundered! {current_gold} gold stolen, {current_people} citizens killed.")

        if city_targets[current_town]['POPULATION'] <= 0 or city_targets[current_town]['GOLD'] <= 0:
            del city_targets[current_town]
            print(f"{current_town} has been wiped off the map!")

    elif action[0] == 'Prosper':
        prosperous_town = action[1]
        growned_gold = int(action[2])

        if growned_gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            city_targets[prosperous_town]['GOLD'] += growned_gold
            print(f"{growned_gold} gold added to the city treasury. "
                  f"{prosperous_town} now has {city_targets[prosperous_town]['GOLD']} gold.")

if len(city_targets) > 0:
    print(f"Ahoy, Captain! There are {len(city_targets)} wealthy settlements to go to:")
    for key, value in city_targets.items():
        town = key
        people = value['POPULATION']
        gold_left = value['GOLD']
        print(f"{town} -> Population: {people} citizens, Gold: {gold_left} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
