amount = 0

while True:
    text = input()
    if text == "NoMoreMoney":
        break

    current_deposit = float(text)

    if current_deposit >= 0:
        amount += current_deposit
        print(f"Increase: {current_deposit:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {amount:.2f}")