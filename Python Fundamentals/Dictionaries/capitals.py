country_names = input().split(", ")
capital_cities = input().split(", ")

city_capitals = dict(zip(country_names, capital_cities))

for country, capital in city_capitals.items():
    print(f"{country} -> {capital}")
