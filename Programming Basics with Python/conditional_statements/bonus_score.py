point_number = int(input())
bonus = 0

if point_number <= 100:
    bonus += 5
elif point_number > 1000:
    bonus += point_number * 0.1
else:
    bonus = point_number * 0.2

if point_number % 2 == 0:
    bonus += 1
elif point_number % 10 == 5:
    bonus += 2

print(bonus)
print(point_number + bonus)
