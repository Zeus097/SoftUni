def boarding_passengers(ship_capacity, *passenger_groups):
    initial_ship_capacity = ship_capacity
    result = ''
    total_pasengers = sum([guest[0] for guest in passenger_groups])
    boarded_passengers = 0
    boarded_guests = {}
    for passengers_num, benefits_program_name in passenger_groups:
        if ship_capacity > 0:
            if ship_capacity >= passengers_num:
                ship_capacity -= passengers_num
                boarded_passengers += passengers_num
                if benefits_program_name not in boarded_guests:
                    boarded_guests[benefits_program_name] = passengers_num
                else:
                    boarded_guests[benefits_program_name] += passengers_num
            else:
                continue
        else:
            break

    sorted_passengers = sorted(boarded_guests.items(), key=lambda x: (-x[1], x[0]))

    result += f"Boarding details by benefit plan:\n"
    for plan_name, guest_num in sorted_passengers:
        result += f"## {plan_name}: {guest_num} guests\n"

    if total_pasengers == boarded_passengers:
        result += "All passengers are successfully boarded!"
    elif not ship_capacity and total_pasengers > boarded_passengers:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    elif ship_capacity and boarded_passengers < total_pasengers:
        available_capacity = initial_ship_capacity - boarded_passengers
        result += f"Partial boarding completed. Available capacity: {available_capacity}."

    return result.strip()


# print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))

# print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'),
# (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))


# print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'),
# (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
