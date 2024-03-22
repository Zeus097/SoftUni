import re

places = input()
travel_points = 0
valid_places = []
pattern = r'(\=|\/)([A-Z][A-Z-a-z]{2,})\1'
matches = re.finditer(pattern, places)

for match in matches:
    travel_points += len(match.group(2))
    valid_places.append(match.group(2))
print(f"Destinations: {', '.join(valid_places)}\nTravel Points: {travel_points}")
