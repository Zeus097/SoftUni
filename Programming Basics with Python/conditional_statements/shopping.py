budget = float(input())
video_card_number = int(input())
processor_number = int(input())
ram_number = int(input())

all_video_card_number_price = video_card_number * 250
one_processor_number_price = all_video_card_number_price * 0.35
all_processor_number_price = one_processor_number_price * processor_number
one_ram_number_price = all_video_card_number_price * 0.1
all_ram_number_price = one_ram_number_price * ram_number

full_price = all_video_card_number_price + all_processor_number_price + all_ram_number_price

if video_card_number > processor_number:
    full_price = full_price * 0.85

remaining_money = abs(budget - full_price)

if budget >= full_price:
    print(f'You have {remaining_money:.2f} leva left!')
else:
    print(f'Not enough money! You need {remaining_money:.2f} leva more!')
