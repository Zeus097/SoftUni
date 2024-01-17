number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed < 1 or capsules_needed > 2000:
        continue
    price = price_per_capsule * days * capsules_needed
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")
