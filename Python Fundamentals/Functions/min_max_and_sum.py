def min_number(numbers):
    return f"The minimum number is {min(numbers)}"
def max_number(numbers):
    return f"The maximum number is {max(numbers)}"
def sum_of_numbers(numbers):
    return f"The sum number is: {sum(numbers)}"

numbers = list(map(int, input().split()))

print(min_number(numbers))
print(max_number(numbers))
print(sum_of_numbers(numbers))
