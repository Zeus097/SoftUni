level_of_fire = input().split("#")
amount_of_water = int(input())
total_fire = 0
total_effort = 0
total_cells = []
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)

for fire in level_of_fire:
    fire_type, cell_value = fire.split(" = ")
    cell_value = int(cell_value)
    cell_is_valid = False

    if fire_type == "High":
        if cell_value in high:
            cell_is_valid = True
    elif fire_type == "Medium":
        if cell_value in medium:
            cell_is_valid = True
    elif fire_type == "Low":
        if cell_value in low:
            cell_is_valid = True

    if cell_is_valid:
        if amount_of_water >= cell_value:
            amount_of_water -= cell_value
            total_effort += cell_value * 0.25
            total_fire += cell_value
            total_cells.append(cell_value)

print("Cells:")
for cell in total_cells:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
