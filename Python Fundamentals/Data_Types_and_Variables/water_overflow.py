capacity = 255
total_liters = 0
number_of_lines = int(input())

for water_tank in range(number_of_lines):
    current_litters = int(input())
    if capacity - current_litters < 0:
        print("Insufficient capacity!")
        continue
    capacity -= current_litters
    total_liters += current_litters

print(total_liters)
