budget = float(input())
needed_fuel_liters = float(input())
day_of_week = input()

fuel_price_per_liter = 2.10
tour_guide = 100

fuel_cost = needed_fuel_liters * fuel_price_per_liter
total_cost = fuel_cost + tour_guide

if day_of_week == "Saturday":
    total_cost *= 0.9
elif day_of_week == "Sunday":
    total_cost *= 0.8

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
