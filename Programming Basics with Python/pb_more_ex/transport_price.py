distance = int(input())
data = input()
taxi_price = 0.70
price = 0
total_sum = 0


if distance >= 20 and distance < 100 :        #bus
    price += 0.09
    total_sum = distance * price
elif distance >= 100:     #train
    price += 0.06
    total_sum = distance * price
else:                     #taxi
    if data == "day":
        price += 0.79
    elif data == "night":
        price += 0.90
    total_sum = taxi_price + distance * price

print(f"{total_sum:.02f}")