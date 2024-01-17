type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
price_per_flower = 0

if type_of_flowers == "Roses":
    price_per_flower = number_of_flowers * 5
    if number_of_flowers > 80:
        price_per_flower *= 0.90
elif type_of_flowers == "Dahlias":
    price_per_flower = number_of_flowers * 3.80
    if number_of_flowers > 90:
        price_per_flower *= 0.85
elif type_of_flowers == "Tulips":
    price_per_flower = number_of_flowers * 2.80
    if number_of_flowers > 80:
        price_per_flower *= 0.85
elif type_of_flowers == "Narcissus":
    price_per_flower = number_of_flowers * 3
    if number_of_flowers < 120:
        price_per_flower *= 1.15
elif type_of_flowers == "Gladiolus":
    price_per_flower = number_of_flowers * 2.50
    if number_of_flowers < 80:
        price_per_flower *= 1.2
needed_sum = abs(price_per_flower - budget)


if budget >= price_per_flower:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {needed_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {needed_sum:.2f} leva more.")