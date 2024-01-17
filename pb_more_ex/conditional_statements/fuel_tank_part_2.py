fuel_type = input()
fuel_quantity = float(input())
club_cart = input()
total_price = 0

if club_cart == "Yes":
    if fuel_type == "Gasoline":
        gasoline_price_per_liter = 2.22 - 0.18
        total_price = gasoline_price_per_liter * fuel_quantity
    elif fuel_type == "Diesel":
        diesel_price_per_liter = 2.33 - 0.12
        total_price = diesel_price_per_liter * fuel_quantity
    elif fuel_type == "Gas":
        gas_price_per_liter = 0.93 - 0.08
        total_price = gas_price_per_liter * fuel_quantity
else:
    if fuel_type == "Gasoline":
        gasoline_price_per_liter = 2.22
        total_price = gasoline_price_per_liter * fuel_quantity
    elif fuel_type == "Diesel":
        diesel_price_per_liter = 2.33
        total_price = diesel_price_per_liter * fuel_quantity
    elif fuel_type == "Gas":
        gas_price_per_liter = 0.93
        total_price = gas_price_per_liter * fuel_quantity

if 20 <= fuel_quantity <= 25:
    total_price *= 0.92
elif fuel_quantity > 25:
    total_price *= 0.90

print(f"{total_price:.02f} lv.")