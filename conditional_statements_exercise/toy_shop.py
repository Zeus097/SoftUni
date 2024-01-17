vacation_price = float(input())
puzzle_number = int(input())
doll_number = int(input())
teddy_bear_number = int(input())
minion_number = int(input())
car_number = int(input())

puzzle_price = puzzle_number * 2.60
doll_price = doll_number * 3
teddy_bear_price = teddy_bear_number * 4.10
minion_price = minion_number * 8.20
car_price = car_number * 2

toys_price = puzzle_price + doll_price + teddy_bear_price + minion_price + car_price
toys_number = puzzle_number + doll_number + teddy_bear_number + minion_number + car_number

if toys_number >= 50:
    toys_price = toys_price * 0.75
else:
    toys_price = toys_price

rent = toys_price * 0.1

earned_money = toys_price - rent
needed_money = abs(earned_money - vacation_price)


if earned_money >= vacation_price:
    print(f'Yes! {needed_money:.02f} lv left.')
else:
    print(f'Not enough money! {needed_money:.02f} lv needed.')