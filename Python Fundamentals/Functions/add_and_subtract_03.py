def add_numbers(num1, num2):
    return num1 + num2
def subtract(result, num3):
    return result - num3
def add_and_subtract(num1, num2, num3):
    result = add_numbers(num1, num2)
    return subtract(result, num3)

first_number, second_number, third_number = int(input()), int(input()), int(input())
print(add_and_subtract(first_number, second_number, third_number))
