from math import floor,ceil

number_of_days = int(input())
provided_food_kg = int(input())
dog_food_for_day_kg = float(input())
cat_food_for_day_kg = float(input())
turtle_food_for_day_gr = float(input())
turtle_food_for_day_kg = turtle_food_for_day_gr / 1000

needed_dog_food = number_of_days * dog_food_for_day_kg
needed_cat_food = number_of_days * cat_food_for_day_kg
needed_turtle_food = number_of_days * turtle_food_for_day_kg
total_needed_food = needed_dog_food + needed_cat_food + needed_turtle_food
extra_food = abs(provided_food_kg - total_needed_food)

if total_needed_food < provided_food_kg:
    extra_food = floor(extra_food)
    print(f"{extra_food} kilos of food left.")
else:
    extra_food = ceil(extra_food)
    print(f"{extra_food} more kilos of food are needed.")