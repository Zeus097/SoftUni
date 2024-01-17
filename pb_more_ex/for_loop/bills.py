months = int(input())
average_fee = 0

electricity_fee = 0
water_fee = 0
net_fee = 0
other_fees = 0
sum_other_fees = 0

for fee in range(months):
    electricity_bill = float(input())
    electricity_fee += electricity_bill
    water_fee = months * 20
    net_fee = months * 15
    sum_electricity_water_net_fee = electricity_bill + 20 + 15
    twenty_percent_of_the_sum = (sum_electricity_water_net_fee * 20) / 100
    other_fees = sum_electricity_water_net_fee + twenty_percent_of_the_sum
    sum_other_fees += other_fees
    average_fee = (electricity_fee + water_fee + net_fee + sum_other_fees) / months

print(f"Electricity: {electricity_fee:.02f} lv")
print(f"Water: {water_fee:.02f} lv")
print(f"Internet: {net_fee:.02f} lv")
print(f"Other: {sum_other_fees:.02f} lv")
print(f"Average: {average_fee:.02f} lv")