group_numbers = int(input())

moussala_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
sum_climbers = 0
for climbers in range(1, group_numbers + 1):
    group_member_number = int(input())
    if group_member_number <= 5:
        moussala_climbers += group_member_number
    elif group_member_number <= 12:
        monblan_climbers += group_member_number
    elif group_member_number <= 25:
        kilimandjaro_climbers += group_member_number
    elif group_member_number <= 40:
        k2_climbers += group_member_number
    elif group_member_number > 40:
        everest_climbers += group_member_number
    sum_climbers += group_member_number

percent_of_moussala_climbers = moussala_climbers / sum_climbers * 100
percent_of_monblan_climbers = monblan_climbers / sum_climbers * 100
percent_of_kilimandjaro_climbers = kilimandjaro_climbers / sum_climbers * 100
percent_of_k2_climbers = k2_climbers / sum_climbers * 100
percent_of_everest_climbers = everest_climbers / sum_climbers * 100

print(f"{percent_of_moussala_climbers:.2f}%")
print(f"{percent_of_monblan_climbers:.2f}%")
print(f"{percent_of_kilimandjaro_climbers:.2f}%")
print(f"{percent_of_k2_climbers:.2f}%")
print(f"{percent_of_everest_climbers:.2f}%")