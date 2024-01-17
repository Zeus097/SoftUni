budget = float(input())
statist_number = int(input())
one_clothes_price = float(input())
decor_price = budget * 0.1

if statist_number > 150:
    one_clothes_price = one_clothes_price * 0.9

clothes_price = statist_number * one_clothes_price

needed_money = decor_price + clothes_price
money_left = abs(budget - needed_money)

if needed_money > budget:
    print('Not enough money!')
    print(f'Wingard needs {money_left:.02f} leva more.')
elif needed_money <= budget:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.02f} leva left.')