days_number = int(input())
hours_number = int(input())
tax = 0
total_sum = 0

for day in range(1, days_number + 1):
    for hour in range(1, hours_number + 1):
        if day % 2 == 0 and hour % 2 != 0:
            tax += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            tax += 1.25
        else:
            tax += 1
    print(f"Day: {day} - {tax:.2f} leva")
    total_sum += tax
    tax = 0
print(f"Total: {total_sum:.2f} leva")
