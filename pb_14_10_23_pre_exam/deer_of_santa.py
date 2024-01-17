from math import floor,ceil

number_of_days_out = int(input())
food = int(input())
first_deer_food = float(input())
second_deer_food = float(input())
third_deer_food = float(input())

first_deer_food *= number_of_days_out
second_deer_food *= number_of_days_out
third_deer_food *= number_of_days_out

total_food = first_deer_food + second_deer_food + third_deer_food

difference = abs(food - total_food)

if food >= total_food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")