strawberries_price = float(input())
banana_in_kg = float(input())
oranges_in_kg = float(input())
raspberry_in_kg = float(input())
strawberries_in_kg = float(input())

raspberry_price = strawberries_price / 2
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2

total_strawberries_price = strawberries_price * strawberries_in_kg
total_raspberry_price = raspberry_price * raspberry_in_kg
total_orange_price = orange_price * oranges_in_kg
total_banana_price = banana_price * banana_in_kg

total_sum = total_strawberries_price + total_raspberry_price + total_orange_price + total_banana_price

print(f"{total_sum:.02f}")
