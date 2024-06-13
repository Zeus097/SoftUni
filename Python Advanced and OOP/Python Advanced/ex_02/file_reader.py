total_sum = 0

with open('numbers.txt') as file:
    for line in file:
        total_sum += int(line)

print(total_sum)
