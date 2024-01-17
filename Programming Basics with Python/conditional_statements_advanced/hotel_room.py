month = input()
number_of_nights = int(input())
apartment = ""
studio = ""

if month == "May" or month == "October":
    studio = number_of_nights * 50
    apartment = number_of_nights * 65
    if number_of_nights > 14:
        studio *= 0.7
        apartment *= 0.9
    elif number_of_nights > 7:
        studio *= 0.95
elif month == "June" or month == "September":
    studio = number_of_nights * 75.20
    apartment = number_of_nights * 68.70
    if number_of_nights > 14:
        studio *= 0.80
        apartment *= 0.90
elif month == "July" or month == "August":
    studio = number_of_nights * 76
    apartment = number_of_nights * 77
    if number_of_nights > 14:
        apartment *= 0.90

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")

