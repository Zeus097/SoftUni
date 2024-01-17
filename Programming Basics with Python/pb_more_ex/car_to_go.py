budget = float(input())
season = input()
class_type = ""
car_type = ""
car_price = 0

if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        car_price = budget * 0.65
elif budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        car_price = budget * 0.80
elif budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    car_price = budget * 0.90

print(class_type)
print(f"{car_type} - {car_price:.02f}")