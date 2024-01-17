#Едно работно място заема 70 на 120 cm

# входната врата (която е с отвор 160 cm) -            1 място
# заради катедрата (която е с размер 160 на 120 cm) -  2 места.



length_in_sm = float(input()) #120
width_in_sm = float(input())  #70
corridor = 100
door_and_department_space = 3

length_in_meters = length_in_sm * 100
width_in_meters = width_in_sm * 100

desk_number = (width_in_meters - corridor) // 70
rolls = length_in_meters // 120
seats_number = (desk_number * rolls) - door_and_department_space
print(f"{seats_number:.0f}")
