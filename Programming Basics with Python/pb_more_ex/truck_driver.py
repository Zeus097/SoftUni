season = input()        #1 season = 4 months
km_per_month = float(input())
current_money = 0

#taxes(10%) are deducted from the money

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        current_money = km_per_month * 0.75
    elif season == "Summer":
        current_money = km_per_month * 0.90
    elif season == "Winter":
        current_money = km_per_month * 1.05
elif km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        current_money = km_per_month * 0.95
    elif season == "Summer":
        current_money = km_per_month * 1.10
    elif season == "Winter":
        current_money = km_per_month * 1.25
elif km_per_month <= 20000:
    current_money = km_per_month * 1.45

salary = (current_money * 4) * 0.9
print(f"{salary:.02f}")