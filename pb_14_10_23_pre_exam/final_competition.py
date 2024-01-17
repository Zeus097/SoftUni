number_of_dancers = int(input())
points = float(input())
season = input()
place = input()
total_money = 0
charity_money = 0

if season == "summer":
    if place == "Bulgaria":
      total_money = number_of_dancers * points
      total_money *= 0.95
    else:  # abroad
        total_money = number_of_dancers * points
        total_money *= 1.5
        total_money *= 0.9

else:      #winter
    if place == "Abroad":
        total_money = number_of_dancers * points
        total_money *= 1.5
        total_money *= 0.85
    else:
        total_money = number_of_dancers * points
        total_money *= 0.92

charity_money = total_money * 0.75
total_money -= charity_money
money_per_dancer = total_money / number_of_dancers

print(f"Charity - {charity_money:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")