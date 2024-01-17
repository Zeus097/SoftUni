upper_limit_hundreds = int(input())
upper_limit_tens = int(input())
upper_limit_units = int(input())
for number in range(1, upper_limit_hundreds + 1):
    if number % 2 == 0:
        for number2 in range(2, upper_limit_tens + 1):
            number2_is_prime = True
            for i in range(2, number2):
                if number2 % i == 0:
                    number2_is_prime = False
                    break
            if number2_is_prime:
                for number3 in range(1, upper_limit_units + 1):
                    if number3 % 2 == 0:
                        print(f"{number} {number2} {number3}")