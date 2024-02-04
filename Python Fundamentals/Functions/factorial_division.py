def factorial_division(num1, num2):
    factorial_num1 = 1
    for factorial in range(1, num1 + 1):
        factorial_num1 *= factorial

    factorial_num2 = 1
    for factorial in range(1, num2 + 1):
        factorial_num2 *= factorial

    factorial = f"{(factorial_num1 // factorial_num2):.2f}"
    return factorial

first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
