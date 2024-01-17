number = int(input())
first_digit_limit = number % 10
second_digit_limit = (number // 10) % 10
third_digit_limit = (number // 100) % 10

for first_digit in range(1, first_digit_limit + 1, 1):
    for second_digit in range(1, second_digit_limit + 1, 1):
        for third_digit in range(1, third_digit_limit + 1, 1):
            result = first_digit * second_digit * third_digit

            print(f"{first_digit} * {second_digit} * {third_digit} = {result};")