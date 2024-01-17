number_of_days = int(input())
total_liters = 0
total_degrees = 0

for days in range(number_of_days):
    alcohol_liters = float(input())
    alcohol_degrees = float(input())
    total_liters += alcohol_liters
    total_degrees += alcohol_degrees * alcohol_liters
average_degrees = total_degrees / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")