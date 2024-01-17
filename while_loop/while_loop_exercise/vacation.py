needed_money = float(input())
own_money = float(input())
days_counter = 0
spending_counter = 0

while own_money < needed_money and spending_counter < 5:
    text = input()
    money = float(input())
    days_counter += 1

    if text == "save":
        own_money += money
        spending_counter = 0
    elif text == "spend":
        own_money -= money
        spending_counter += 1
        if own_money < 0:
            own_money = 0

    if spending_counter == 5:
        print("You can't save the money.")
        print(days_counter)
    if own_money >= needed_money:
        print(f"You saved the money for {days_counter} days.")