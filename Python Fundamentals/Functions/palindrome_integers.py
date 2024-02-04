def is_palindrome(numbers):
    for num in numbers:
        if num == num[::-1]:
            print(True)
        else:
            print(False)
numbers = list(input().split(", "))

is_palindrome(numbers)
