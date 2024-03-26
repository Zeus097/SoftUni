tour_stops = input()

while True:
    command = input()
    if command == 'Travel':
        break

    action = command.split(':')
    if action[0] == 'Add Stop':
        index = int(action[1])
        string = action[2]
        if index <= len(tour_stops) - 1:
            tour_stops = tour_stops[:index] + string + tour_stops[index:]

    elif action[0] == 'Remove Stop':
        start_index = int(action[1])
        end_index = int(action[2])
        if start_index <= len(tour_stops) - 1 >= end_index:
            tour_stops = tour_stops.replace(tour_stops[start_index:end_index + 1], '')

    elif action[0] == 'Switch':
        old_string = action[1]
        new_string = action[2]
        if old_string in tour_stops:
            tour_stops = tour_stops.replace(old_string, new_string)
    print(tour_stops)

print(f"Ready for world tour! Planned stops: {tour_stops}")
