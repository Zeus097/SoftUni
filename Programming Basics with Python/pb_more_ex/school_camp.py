season = input()
gender = input()
student_number = int(input())
day_number = int(input())
sport_type = ""
current_price = 0

if season == "Winter":
    if gender == "girls":
        current_price = (student_number * 9.60) * day_number
        sport_type = "Gymnastics"
    elif gender == "boys":
        current_price = (student_number * 9.60) * day_number
        sport_type = "Judo"
    elif gender == "mixed":
        current_price = (student_number * 10) * day_number
        sport_type = "Ski"
elif season == "Spring":
    if gender == "girls":
        current_price = (student_number * 7.20) * day_number
        sport_type = "Athletics"
    elif gender == "boys":
        current_price = (student_number * 7.20) * day_number
        sport_type = "Tennis"
    elif gender == "mixed":
        current_price = (student_number * 9.50) * day_number
        sport_type = "Cycling"
elif season == "Summer":
    if gender == "girls":
        current_price = (student_number * 15) * day_number
        sport_type = "Volleyball"
    elif gender == "boys":
        current_price = (student_number * 15) * day_number
        sport_type = "Football"
    elif gender == "mixed":
        current_price = (student_number * 20) * day_number
        sport_type = "Swimming"

if student_number >= 50:
    current_price *= 0.5
elif 50 > student_number >= 20:
    current_price *= 0.85
elif 20 > student_number >= 10:
    current_price *= 0.95

print(f"{sport_type} {current_price:.02f} lv.")