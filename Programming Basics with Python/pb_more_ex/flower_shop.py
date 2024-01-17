from math import ceil,floor

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cactus_price = 8
tax = 0.95

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cactus = int(input())
present_price = float(input())

magnolias_profit = number_of_magnolias * magnolias_price
hyacinths_profit = number_of_hyacinths * hyacinths_price
roses_profit = number_of_roses * roses_price
cactus_profit = number_of_cactus * cactus_price
total_profit = (magnolias_profit + hyacinths_profit + roses_profit + cactus_profit) * tax

diff = abs(present_price - total_profit)


if total_profit >= present_price :
    needed_money = floor(diff)
    print(f"She is left with {needed_money} leva.")
else:
    needed_money = ceil(diff)
    print(f"She will have to borrow {needed_money} leva.")