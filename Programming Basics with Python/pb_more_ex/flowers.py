chrysanthemums_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
weekend_day = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
arranging_bouquet_price = 2
flowers_number = 0
flowers_sum = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = chrysanthemums_number * 2.00
    roses_price = roses_number * 4.10
    tulips_price = tulips_number * 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = chrysanthemums_number * 3.75
    roses_price = roses_number * 4.50
    tulips_price = tulips_number * 4.15
flowers_sum = chrysanthemums_price + roses_price + tulips_price

if weekend_day == "Y":
    flowers_sum *= 1.15

if tulips_number > 7 and season == "Spring":
    flowers_sum *= 0.95
elif roses_number >= 10 and season == "Winter":
    flowers_sum *= 0.9

flowers_number = chrysanthemums_number + roses_number + tulips_number
if flowers_number > 20:
    flowers_sum *= 0.80

flowers_sum += arranging_bouquet_price

print(f"{flowers_sum:.02f}")