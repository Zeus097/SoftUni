def calculating_orders(product, quantity):
    if product == "coffee":
        return f"{quantity * 1.50:.2f}"
    elif product == "water":
        return f"{quantity * 1.00:.2f}"
    elif product == "coke":
        return f"{quantity * 1.40:.2f}"
    elif product == "snacks":
        return f"{quantity * 2.00:.2f}"

product = input()
quantity = int(input())

print(calculating_orders(product, quantity))
