fuel_type = input()
fuel_available = float(input())

if fuel_available >= 25:
    if fuel_type == "Diesel":
        print("You have enough diesel.")
    elif fuel_type == "Gasoline":
        print("You have enough gasoline.")
    elif fuel_type == "Gas":
        print("You have enough gas.")
else:
    if fuel_type == "Diesel":
        print("Fill your tank with diesel!")
    elif fuel_type == "Gasoline":
        print("Fill your tank with gasoline!")
    elif fuel_type == "Gas":
        print("Fill your tank with gas!")

if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")
