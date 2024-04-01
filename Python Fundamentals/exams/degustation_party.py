information = {}
unliked_meals = 0

while True:
    command = input()
    if command == 'Stop':
        break

    action = command.split('-')
    if action[0] == 'Like':
        guest = action[1]
        meal = action[2]
        if guest not in information:
            information[guest] = []

        if meal in information[guest]:
            continue

        information[guest].append(meal)

    elif action[0] == 'Dislike':
        guest = action[1]
        meal = action[2]
        if guest not in information.keys():
            print(f"{guest} is not at the party.")

        elif meal not in information[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            information[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            unliked_meals += 1

for info in information.keys():
    current_guest = info
    current_meal = ', '.join(information[current_guest])
    print(f"{current_guest}: {current_meal}")

print(f"Unliked meals: {unliked_meals}")
