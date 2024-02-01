numbers = input().split()
rounded_numbers = []

for num in numbers:
    rounded_numbers.append(round(float(num)))

print(rounded_numbers)
