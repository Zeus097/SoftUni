budget = int(input())
season = input()
number_of_fishermen = int(input())
boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if number_of_fishermen <= 6:
    boat_price *= 0.9
elif number_of_fishermen <= 11:
    boat_price *= 0.85
else:
    boat_price *= 0.75

if number_of_fishermen % 2 == 0 and season != "Autumn":
    boat_price *= 0.95

difference = abs(budget - boat_price)

if budget >= boat_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")