number = int(input())

# Print the top row of asterisks
print('*' * number)

# Print the middle rows with a hollow center
for i in range(2, number):
    print('*' + ' ' * (number - 2) + '*')

# Print the bottom row of asterisks
if number > 1:
    print('*' * number)
