def plant_discovery(number):
    collection = {}
    for plant_index in range(number):
        command_line = input().split('<->')
        plant = command_line[0]
        rarity = int(command_line[1])
        collection[plant] = {'RARITY': rarity, 'RATING': []}

    return collection


def exhibition(collection):
    while True:
        command = input()
        if command == 'Exhibition':
            break

        action = command.split(': ')
        if action[0] == 'Rate':
            plant_information = action[1].split(' - ')
            plant_name = plant_information[0]
            if plant_name not in collection:
                print('error')
                continue
            plant_rating = int(plant_information[1])
            collection[plant_name]['RATING'].append(plant_rating)

        elif action[0] == 'Update':
            plant_information = action[1].split(' - ')
            plant_name = plant_information[0]
            if plant_name not in collection:
                print('error')
                continue
            new_rarity = int(plant_information[1])
            collection[plant_name]['RARITY'] = new_rarity

        elif action[0] == 'Reset':
            plant_name = action[1]
            if plant_name not in collection:
                print('error')
                continue
            collection[plant_name]['RATING'].clear()

    return collection


def plant_discovery_output(plants):
    print("Plants for the exhibition: ")
    for plant in plants:
        rarity = plants[plant]['RARITY']
        rating_info = plants[plant]['RATING']
        average_rating = 0
        if rating_info:
            average_rating += sum(rating_info) / len(rating_info)
        print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


discovery_number = int(input())
pland_collection = plant_discovery(discovery_number)
plant_info = exhibition(pland_collection)
plant_discovery_output(plant_info)
