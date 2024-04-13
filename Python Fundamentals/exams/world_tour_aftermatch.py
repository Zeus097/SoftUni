def planning_stops(places):
    while True:
        command = input()
        if command == 'Travel':
            break

        action = command.split(':')
        if action[0] == 'Add Stop':
            index = int(action[1])
            string = action[2]
            if 0 <= index < len(places):
                places = places[:index] + string + places[index:]

        elif action[0] == 'Remove Stop':
            start_index = int(action[1])
            end_index = int(action[2])
            if start_index < len(places) > end_index:
                places = places.replace(places[start_index:end_index + 1], '')

        elif action[0] == 'Switch':
            old_string = action[1]
            new_string = action[2]
            if old_string in places:
                places = places.replace(old_string, new_string)
        print(places)
    print(f"Ready for world tour! Planned stops: {places}")


total_stops = input()
planning_stops(total_stops)
