budget = float(input())
category = input()
number_of_people = int(input())
category_price = 0

if 1 <= number_of_people <= 4:
    budget *= 0.25
elif number_of_people <= 9:
    budget *= 0.4
elif number_of_people <= 24:
    budget *= 0.5
elif number_of_people <= 49:
    budget *= 0.6
else:
    budget *= 0.75

if category == "VIP":
    category_price = number_of_people * 499.99
elif category == "Normal":
    category_price = number_of_people * 249.99

diff = abs(category_price - budget)

if budget >= category_price:
    print(f"Yes! You have {diff:.02f} leva left.")
else:
    print(f"Not enough money! You need {diff:.02f} leva.")
