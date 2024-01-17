days = int(input())
room_type = input()
rating = input()
number_of_nights = days - 1

if room_type == "room for one person":
    room_type = number_of_nights * 18.00
elif room_type == "apartment":
    room_type = number_of_nights * 25.00
    if days < 10:
        room_type *= 0.70
    elif 10 < days <= 15:
        room_type *= 0.65
    elif days > 15:
        room_type *= 0.5
elif room_type == "president apartment":
    room_type = number_of_nights * 35.00
    if days < 10:
        room_type *= 0.90
    elif 10 < days <= 15:
        room_type *= 0.85
    elif days > 15:
        room_type *= 0.80

if rating == "positive":
    room_type *= 1.25
    print(f"{room_type:.02f}")
elif rating == "negative":
    room_type *= 0.9
    print(f"{room_type:.02f}")
