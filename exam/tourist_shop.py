budget = float(input())
counter = 0
total_sum = 0
enough = False

while True:
    product_name = input()

    if product_name == "Stop":
        enough = True
        break

    product_price = float(input())

    counter += 1
    if counter % 3 == 0:
        product_price /= 2

    total_sum += product_price
    if total_sum > budget:
        break

if enough:
    print(f"You bought {counter} products for {total_sum:.2f} leva.")
else:
    difference = abs(budget - total_sum)
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")
