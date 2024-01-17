shoes = int(input())
annual_fee = shoes

shoes_price = shoes - (shoes * 0.4)
training_suit_price = shoes_price - (shoes_price * 0.2)
ball_price = training_suit_price / 4
accessories_price = ball_price / 5

total_sum = annual_fee + shoes_price + training_suit_price + ball_price + accessories_price

print(total_sum)
