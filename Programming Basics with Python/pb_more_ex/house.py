number = int(input())

# Print the roof

for i in range(1, (number + 1) // 2 + 1):
    asterisks = '*' * (1 if number % 2 == 1 else 2)
    if number % 2 != 0:
        print('-' * ((number - 1) // 2 - i + 1) + asterisks * (2 * i - 1) + '-' * ((number - 1) // 2 - i + 1))
    else:
        asterisks = '*'
        print('-' * ((number - 1) // 2 - i + 1) + asterisks * (2 * i) + '-' * ((number - 1) // 2 - i + 1))
# Print the base

for i in range(number // 2):
    print('|' + '*' * (number - 2) + '|')

