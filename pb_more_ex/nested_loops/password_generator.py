first_digit = int(input())
second_digit = int(input())

for digit1 in range(1, first_digit + 1):
    for digit2 in range(1, first_digit + 1):
        for letter3 in range(ord('a'), ord('a') + second_digit):
            for letter4 in range(ord('a'), ord('a') + second_digit):
                for digit5 in range(max(digit1, digit2) + 1, first_digit + 1):
                    password = f"{digit1}{digit2}{chr(letter3)}{chr(letter4)}{digit5}"

                    print(password, end=" ")
