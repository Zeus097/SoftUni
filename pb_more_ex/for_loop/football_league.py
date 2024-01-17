stadium_capacity = int(input())
number_of_fans = int(input())

sector_A_counter = 0
sector_B_counter = 0
sector_V_counter = 0
sector_G_counter = 0

sector_A_percentage = 0
sector_B_percentage = 0
sector_V_percentage = 0
sector_G_percentage = 0

for fan in range(number_of_fans):
    sector_name = input()
    if sector_name == "A":
         sector_A_counter += 1
    elif sector_name == "B":
        sector_B_counter += 1
    elif sector_name == "V":
        sector_V_counter += 1
    elif sector_name == "G":
        sector_G_counter += 1

    sector_A_percentage = sector_A_counter / number_of_fans * 100
    sector_B_percentage = sector_B_counter / number_of_fans * 100
    sector_V_percentage = sector_V_counter / number_of_fans * 100
    sector_G_percentage = sector_G_counter / number_of_fans * 100

total_fans_percentage = number_of_fans / stadium_capacity * 100

print(f"{sector_A_percentage:.02f}%")
print(f"{sector_B_percentage:.02f}%")
print(f"{sector_V_percentage:.02f}%")
print(f"{sector_G_percentage:.02f}%")
print(f"{total_fans_percentage:.02f}%")