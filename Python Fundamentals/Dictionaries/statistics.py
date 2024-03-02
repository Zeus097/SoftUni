statistics = {}

while True:
    keys_and_values = input().split(": ")

    if keys_and_values[0] == "statistics":
        break

    product, quantity = keys_and_values[0], int(keys_and_values[1])
    if product not in statistics:
        statistics[product] = 0
    statistics[product] += quantity

print("Products in stock:")
for key, value in statistics.items():
    print(f"- {key}: {value}")

total_products = len(statistics)
total_quantity = sum(statistics.values())

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
