import re


places_on_the_map = input()
travel_points = 0
destination_collection = []
pattern = r'([=/])([A-Z]{1}[A-Za-z]{2,})\1'
matches = re.findall(pattern, places_on_the_map)
for match in matches:
    current_destination = match[1]
    travel_points += len(current_destination)
    destination_collection.append(current_destination)


print(f"Destinations: {', '.join(destination_collection)}")
print(f"Travel Points: {travel_points}")
