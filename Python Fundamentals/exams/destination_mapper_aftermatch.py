import re


def validateing_places(destinations):
    valid_destinations = []
    pattern = r'([=/])([A-Z]{1}[A-Za-z]{2,})\1'
    matches = re.findall(pattern, destinations)
    for match in matches:
        current_destination = match[1]
        valid_destinations.append(current_destination)
    return valid_destinations


def calculating_travel_points(destinations):
    points = 0
    for destination in destinations:
        points += len(destination)

    return points


places = input()
valid_places = validateing_places(places)
travel_points = calculating_travel_points(valid_places)

print(f"Destinations: {', '.join(valid_places)}")
print(f"Travel Points: {travel_points}")
