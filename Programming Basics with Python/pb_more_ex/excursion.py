sea_vacation = int(input())
mountain_vacation = int(input())
command = input()
total_money = 0
current_price = 0
sold_out = False

while command != "Stop":
    package_name = command

    if package_name == "sea" and sea_vacation > 0:
        current_price = 680
        total_money += current_price
        sea_vacation -= 1
    elif package_name == "mountain" and mountain_vacation > 0:
        current_price = 499
        total_money += current_price
        mountain_vacation -= 1

    if sea_vacation == 0 and mountain_vacation == 0:
        sold_out = True
        break
    command = input()


if sold_out:
    print("Good job! Everything is sold.")

print(f"Profit: {total_money} leva.")