budget = float(input())
season = input()
location = ""
country = ""
current_price = 0

if budget <= 1000:
    location = "Camp"
    if season == "Summer":
        country = "Alaska"
        current_price = budget * 0.65
    elif season == "Winter":
        country = "Morocco"
        current_price = budget * 0.45
elif budget <= 3000:
    location = "Hut"
    if season == "Summer":
        country = "Alaska"
        current_price = budget * 0.80
    elif season == "Winter":
        country = "Morocco"
        current_price = budget * 0.60
elif budget > 3000:
    location = "Hotel"
    current_price = budget * 0.90
    if season == "Summer":
        country = "Alaska"
    elif season == "Winter":
        country = "Morocco"

print(f"{country} - {location} - {current_price:.02f}")