items_input = input().split("|")
budget = float(input())
prices = {"Clothes": 50.00, "Shoes": 35.00, "Accessories": 20.50}
bought_items = []
total_profit = 0
ticket_price = 150

for item in items_input:
    item_info = item.split("->")
    item_type, item_price = item_info[0], float(item_info[1])

    if prices[item_type] >= item_price and budget >= item_price:
        budget -= item_price
        bought_items.append(item_price)
        total_profit += item_price * 0.4

budget += total_profit
new_prices = [f'{price * 1.4:.2f}' for price in bought_items]

print(" ".join(new_prices))
print(f"Profit: {total_profit:.2f}")

if budget + sum(bought_items) >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
