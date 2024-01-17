juniors_number = int(input())
seniors_number = int(input())
road_type = input()

cyclist_counter = juniors_number + seniors_number
expenses = 0.05
current_price_juniors = 0
current_price_seniors = 0
fee = 0
donated_sum = 0

if road_type == "trail":
    current_price_juniors = juniors_number * 5.50
    current_price_seniors = seniors_number * 7
elif road_type == "cross-country":
    current_price_juniors = juniors_number * 8
    current_price_seniors = seniors_number * 9.50
elif road_type == "downhill":
    current_price_juniors = juniors_number * 12.25
    current_price_seniors = seniors_number * 13.75
elif road_type == "road":
    current_price_juniors = juniors_number * 20
    current_price_seniors = seniors_number * 21.50

fee = (current_price_juniors + current_price_seniors)

if cyclist_counter >= 50 and road_type == "cross-country":
    fee *= 0.75

expenses *= fee
donated_sum = fee - expenses

print(f"{donated_sum:.02f}")
