def positive_numbers(numbers):
    positive_numbers = [digit for digit in numbers if digit >= 0]
    message = ", ".join(str(digit) for digit in positive_numbers)
    result = f"Positive: {message}"
    return result


def negative_numbers(numbers):
    negative_numbers = [digit for digit in numbers if digit < 0]
    message = ", ".join(str(digit) for digit in negative_numbers)
    result = f"Negative: {message}"
    return result


def even_numbers(numbers):
    even_numbers = [digit for digit in numbers if digit % 2 == 0]
    message = ", ".join(str(digit) for digit in even_numbers)
    result = f"Even: {message}"
    return result


def odd_numbers(numbers):
    odd_numbers = [digit for digit in numbers if digit % 2 != 0]
    message = ", ".join(str(digit) for digit in odd_numbers)
    result = f"Odd: {message}"
    return result



numbers = list(map(int, input().split(", ")))
positive_result = positive_numbers(numbers)
negative_result = negative_numbers(numbers)
even_result = even_numbers(numbers)
odd_result = odd_numbers(numbers)

print(positive_result)
print(negative_result)
print(even_result)
print(odd_result)
