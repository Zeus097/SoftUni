inherited_money = float(input())
year_to_live = int(input())
money_left = 0
years_old = 18

for past in range(1800, year_to_live + 1):
    if past % 2 == 0:
        money_left -= 12000
    else:
        money_left -= 12000 + (50 * years_old)
    years_old += 1
money_left += inherited_money
if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    money_left = abs(money_left)
    print(f"He will need {money_left:.2f} dollars to survive.")