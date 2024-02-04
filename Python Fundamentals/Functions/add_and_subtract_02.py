def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(result, num3):
    return result - num3

def add_and_subtract_numbers(num1, num2, num3):
    add_numbers(num1, num2)
    result = subtract_numbers(num1, num3)
    return result

first_number, second_number, third_number = int(input()), int(input()), int(input())

result = add_numbers(first_number, second_number) - third_number
print(result)
