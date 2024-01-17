needed_sum = int(input())
counter_payment = 0
cash_counter = 0
card_counter = 0
cash_payment = 0
card_payment = 0
total_sum = 0
average_payment_cash = 0
average_payment_card = 0
command = input()

while command != "End":
    current_product_price = int(command)
    counter_payment += 1
    if counter_payment % 2 == 1:
        if current_product_price > 100:
            print("Error in transaction!")
        else:
            cash_payment += current_product_price
            cash_counter += 1
            print("Product sold!")
    else:
        if current_product_price < 10:
            print("Error in transaction!")
        else:
            card_payment += current_product_price
            card_counter += 1
            print("Product sold!")

    total_sum = cash_payment + card_payment

    if total_sum >= needed_sum:
        average_payment_cash = cash_payment / cash_counter
        average_payment_card = card_payment / card_counter
        print(f"Average CS: {average_payment_cash:.02f}")
        print(f"Average CC: {average_payment_card:.02f}")
        break

    command = input()

if command == "End":
    print("Failed to collect required money for charity.")