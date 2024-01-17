contract_period = input()
contract_type = input()
add_mobile_internet = input()
tax_period = int(input())
price = 0
discount = 0

if contract_period == "one":
    if contract_type == "Small":
        price += 9.98
    elif contract_type == "Middle":
        price += 18.99
    elif contract_type == "Large":
        price += 25.98
    elif contract_type == "ExtraLarge":
        price += 35.99

elif contract_period == "two":
    if contract_type == "Small":
        price += 8.58
    elif contract_type == "Middle":
        price += 17.09
    elif contract_type == "Large":
        price += 23.59
    elif contract_type == "ExtraLarge":
        price += 31.79

if add_mobile_internet == "yes":
    if price <= 10.00:
        price += 5.50
    elif price <= 30.00:
        price += 4.35
    elif price > 30.00:
        price += 3.85

if contract_period == "two":
    discount = price * 0.0375

price -= discount
price *= tax_period

print(f"{price:.2f} lv.")
