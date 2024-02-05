def multiplication_sign(num1, num2, num3):
    sum = num1 * num2 * num3
    if sum == 0:
        return "zero"
    elif sum < 0:
        return "negative"
    elif sum > 0:
        return "positive"

first_number, second_number, third_number = int(input()), int(input()), int(input())
print(multiplication_sign(first_number, second_number, third_number))
