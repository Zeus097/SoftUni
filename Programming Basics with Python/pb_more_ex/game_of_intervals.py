number_of_moves = int(input())
total_result = 0

zero_to_nine_counter = 0
ten_to_nineteen_counter = 0
twenty_to_twenty_nine_counter = 0
thirty_to_thirty_nine_counter = 0
forty_to_fifty_counter = 0
invalid_number_counter = 0

zero_to_nine_percentage = 0
ten_to_nineteen_percentage = 0
twenty_to_twenty_nine_percentage = 0
thirty_to_thirty_nine_percentage = 0
forty_to_fifty_percentage = 0
invalid_number_percentage = 0

for result in range(number_of_moves):
    new_number = int(input())
    if 0 <= new_number <= 9:
        total_result += new_number * 0.2
        zero_to_nine_counter += 1
    elif 10 <= new_number <= 19:
        total_result += new_number * 0.3
        ten_to_nineteen_counter += 1
    elif 20 <= new_number <= 29:
        total_result += new_number * 0.4
        twenty_to_twenty_nine_counter += 1
    elif 30 <= new_number <= 39:
        total_result += 50
        thirty_to_thirty_nine_counter += 1
    elif 40 <= new_number <= 50:
        total_result += 100
        forty_to_fifty_counter += 1
    elif new_number > 50 or new_number < 0:
        total_result /= 2
        invalid_number_counter += 1
    zero_to_nine_percentage = zero_to_nine_counter / number_of_moves * 100
    ten_to_nineteen_percentage = ten_to_nineteen_counter / number_of_moves * 100
    twenty_to_twenty_nine_percentage = twenty_to_twenty_nine_counter / number_of_moves * 100
    thirty_to_thirty_nine_percentage = thirty_to_thirty_nine_counter / number_of_moves * 100
    forty_to_fifty_percentage = forty_to_fifty_counter / number_of_moves * 100
    invalid_number_percentage = invalid_number_counter / number_of_moves * 100

print(f"{total_result:.02f}")
print(f"From 0 to 9: {zero_to_nine_percentage:.02f}%")
print(f"From 10 to 19: {ten_to_nineteen_percentage:.02f}%")
print(f"From 20 to 29: {twenty_to_twenty_nine_percentage:.02f}%")
print(f"From 30 to 39: {thirty_to_thirty_nine_percentage:.02f}%")
print(f"From 40 to 50: {forty_to_fifty_percentage:.02f}%")
print(f"Invalid numbers: {invalid_number_percentage:.02f}%")