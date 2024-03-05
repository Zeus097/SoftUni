products = {}

while True:
    command = input()

    if command == "buy":
        break

    product_data = command.split()

    for index in range(0, len(product_data), 3):
        name = product_data[index]
        price = float(product_data[index + 1])
        quantity = int(product_data[index + 2])

        if name not in products.keys():
            products[name] = [price, quantity]

        else:
            products[name][1] += quantity
            if price not in products[name]:
                products[name][0] = price

for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
