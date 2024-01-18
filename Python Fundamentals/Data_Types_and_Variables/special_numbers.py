number = int(input())

for current_number in range(1, number + 1):
    is_special = False
    sum_digits_sum = 0
    for digit in str(current_number):
        sum_digits_sum += int(digit)
    if sum_digits_sum == 5 or sum_digits_sum == 7 or sum_digits_sum == 11:
        is_special = True
    if is_special:
        print(f"{current_number} -> {is_special}")
    else:
        print(f"{current_number} -> {is_special}")
