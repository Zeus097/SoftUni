number = int(input())
p1_counter = 0
p2_counter = 0
p3_counter = 0

for num in range(1, number + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        p1_counter += 1
    if current_number % 3 == 0:
        p2_counter += 1
    if current_number % 4 == 0:
        p3_counter += 1

p1_percentage = (p1_counter / number) * 100
p2_percentage = (p2_counter / number) * 100
p3_percentage = (p3_counter / number) * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
