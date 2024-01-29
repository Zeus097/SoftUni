string = input().split()
opposite_numbers = []

for number in string:
    current_number = -int(number)
    opposite_numbers.append(current_number)

print(opposite_numbers)
