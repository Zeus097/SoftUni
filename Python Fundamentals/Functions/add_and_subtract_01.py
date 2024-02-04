def sum_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(num3):
    return num3
def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2) - subtract_numbers(num3)
    return result

first_number, second_number, third_number = int(input()), int(input()), int(input())

print(add_and_subtract(first_number, second_number, third_number))
