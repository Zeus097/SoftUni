def calculating_special(total_price_without_taxes, total_amount_of_taxes):
    """
    If the customer is special, he has a 10% discount on the total price with taxes.
    """

    final_price = (total_price_without_taxes + total_amount_of_taxes)
    special_discount = final_price * 0.1
    special_price = final_price - special_discount

    return special_price


def calculating_regular(total_price_without_taxes, total_amount_of_taxes):
    final_price = total_price_without_taxes + total_amount_of_taxes
    return final_price


command = input()
total_amount_of_taxes = 0
total_price_without_taxes = 0
total_price = 0

while True:
    if command == "special" or command == "regular":
        break
    current_money = float(command)

    if current_money < 0:
        print("Invalid price!")
        command = input()
        continue

    total_price_without_taxes += current_money
    total_amount_of_taxes = total_price_without_taxes * 0.2
    command = input()

if command == "special":
    total_price += calculating_special(total_price_without_taxes, total_amount_of_taxes)
elif command == "regular":
    total_price += calculating_regular(total_price_without_taxes, total_amount_of_taxes)

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
