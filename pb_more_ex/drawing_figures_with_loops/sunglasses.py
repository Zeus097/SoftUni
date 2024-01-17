number = int(input())

# Top row

top_row = '*' * (2 * number) + ' ' * number + '*' * (2 * number)
print(top_row)

# Middle rows

for i in range(number - 2):
    middle_row = '*' + '/' * (2 * number - 2) + '*' + ' ' * number + '*' + '/' * (2 * number - 2) + '*'
    if i == (number - 1) // 2 - 1:
        middle_row = '*' + '/' * (2 * number - 2) + '*' + '|' * number + '*' + '/' * (2 * number - 2) + '*'
    print(middle_row)

# Bottom row

bottom_row = '*' * (2 * number) + ' ' * number + '*' * (2 * number)
print(bottom_row)