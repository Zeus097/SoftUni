chiken_menu_number = int(input())
fish_menu_number = int(input())
vegetarian_menu_number = int(input())


chiken_price = chiken_menu_number * 10.35
fish_price = fish_menu_number * 12.40
vegetarian_price = vegetarian_menu_number * 8.15
delivery_price = 2.50

menu_price = chiken_price + fish_price + vegetarian_price
desert = menu_price * 0.2

sum = menu_price + desert + delivery_price

print(sum)



