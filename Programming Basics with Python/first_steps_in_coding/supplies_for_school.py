pen_package = float(input())
markers_package = float(input())
desk_cleaner = float(input())
discount = float(input())

pens_cost = pen_package * 5.80
markers_cost = markers_package * 7.20
desk_cleaner_cost = desk_cleaner * 1.20

price_withought_discount = pens_cost + markers_cost + desk_cleaner_cost
price_with_discount = price_withought_discount - (price_withought_discount * discount) / 100


print(price_with_discount)
