number = int(input())

left_right = (number - 1) // 2

# Print the top half of the diamond

for i in range(0, (number + 1) // 2):
    mid = number - 2 * left_right - 2
    if mid >= 0:
        row = '-' * left_right + '*' + '-' * mid + '*' + '-' * left_right
    else:
        row = '-' * left_right + '*' + '-' * left_right
    print(row.center(number))

    left_right -= 1

# Print the bottom half of the diamond

left_right = 1
for i in range((number - 1) // 2 - 1, -1, -1):
    mid = number - 2 * left_right - 2
    if mid >= 0:
        row = '-' * left_right + '*' + '-' * mid + '*' + '-' * left_right
    else:
        row = '-' * left_right + '*' + '-' * left_right
    print(row.center(number))

    left_right += 1
