budget = float(input())
season = input()
needed_money = 0
destination = ""
type_of_vacation = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        needed_money = budget * 1.3
        type_of_vacation = "Camp"
    elif season == "winter":
        needed_money = budget * 1.7
        type_of_vacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        needed_money = budget * 1.4
        type_of_vacation = "Camp"
    elif season == "winter":
        needed_money = budget * 1.8
        type_of_vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    needed_money = budget * 1.9
    type_of_vacation = "Hotel"
difference = abs(budget - needed_money)

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {difference:.2f}")