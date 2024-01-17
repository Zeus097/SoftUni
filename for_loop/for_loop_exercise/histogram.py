data = int(input())
p1_range = 0
p2_range = 0
p3_range = 0
p4_range = 0
p5_range = 0

for number in range(data):
    current_number = int(input())
    if current_number < 200:
        p1_range += 1
    elif current_number < 400:
        p2_range += 1
    elif current_number < 600:
        p3_range += 1
    elif current_number < 800:
        p4_range += 1
    elif current_number >= 800:
        p5_range += 1

percent_of_p1_range = p1_range / data * 100
percent_of_p2_range = p2_range / data * 100
percent_of_p3_range = p3_range / data * 100
percent_of_p4_range = p4_range / data * 100
percent_of_p5_range = p5_range / data * 100

print(f"{percent_of_p1_range:.2f}%")
print(f"{percent_of_p2_range:.2f}%")
print(f"{percent_of_p3_range:.2f}%")
print(f"{percent_of_p4_range:.2f}%")
print(f"{percent_of_p5_range:.2f}%")