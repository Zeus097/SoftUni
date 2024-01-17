age = int(input())
laundry_price = float(input())
price_per_toy = int(input())
total_money = 0
total_toys = 0
birthday_money = 0

for birthday in range(1, age +1):
    if birthday % 2 == 0:
        birthday_money += 10
        total_money += birthday_money - 1
    else:
        total_toys += 1

total_money += price_per_toy * total_toys
diff = abs(total_money - laundry_price)

if total_money >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
