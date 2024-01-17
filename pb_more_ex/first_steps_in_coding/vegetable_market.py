vegetables_price = float(input())
fruits_price = float(input())
vegetables_kilograms = int(input())
fruits_kilograms = int(input())
euro = 1.94
sum_vegetables = vegetables_price * vegetables_kilograms
sum_fruits = fruits_price * fruits_kilograms
total_sum = (sum_vegetables + sum_fruits) / euro

print(f"{total_sum:.2f}")
