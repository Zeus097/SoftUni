number = int(input())
plants_information = {}

for index in range(number):
    plant, rarity = input().split('<->')
    plants_information[plant] = {'RARITY': rarity, 'RATING': []}

while True:
    command = input()
    if command == 'Exhibition':
        break

    action = command.split(': ')
    needed_plant_information = action[1].split(' - ')
    plant_info = needed_plant_information[0]

    if plant_info not in plants_information:
        print('error')
        continue

    if action[0] == 'Rate':
        info = action[1].split(' - ')
        current_plant = info[0]
        current_raiting = int(info[1])
        plants_information[current_plant]['RATING'].append(current_raiting)

    elif action[0] == 'Update':
        info = action[1].split(' - ')
        current_plant = info[0]
        new_rarity = int(info[1])
        plants_information[current_plant]['RARITY'] = new_rarity

    elif action[0] == 'Reset':
        current_plant = action[1]
        plants_information[current_plant]['RATING'].clear()

print('Plants for the exhibition:')
for plant in plants_information:
    rating_info = plants_information[plant]['RATING']
    plant_name = plant
    plant_rarity = plants_information[plant]['RARITY']
    average_rating = 0
    if rating_info:
        average_rating += sum(rating_info) / len(rating_info)

    print(f'- {plant_name}; Rarity: {plant_rarity}; Rating: {average_rating:.2f}')
