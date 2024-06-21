rows, cols = list(map(int, input().split(',')))

cupboard = []
mouse_position = None
total_cheese = 0

for i in range(rows):
    data = list(input())
    cupboard.append(data)
    if 'M' in data:
        j = data.index('M')
        mouse_position = (i, j)

    for cheese in data:
        if 'C' == cheese:
            total_cheese += 1


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    command = input()
    if command == 'danger':
        if total_cheese:
            print("Mouse will come back later!")
        break

    current_row = mouse_position[0]
    current_col = mouse_position[1]

    next_row = current_row + directions[command][0]
    next_col = current_col + directions[command][1]

    if 0 <= next_row < len(cupboard) and 0 <= next_col < len(cupboard[0]):
        if cupboard[next_row][next_col] == 'C':
            mouse_position = (next_row, next_col)
            cupboard[next_row][next_col] = 'M'
            cupboard[current_row][current_col] = '*'
            total_cheese -= 1
            if total_cheese == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break

        elif cupboard[next_row][next_col] == 'T':
            mouse_position = (next_row, next_col)
            cupboard[next_row][next_col] = 'M'
            cupboard[current_row][current_col] = '*'
            print("Mouse is trapped!")
            break

        elif cupboard[next_row][next_col] == '*':
            mouse_position = (next_row, next_col)
            cupboard[next_row][next_col] = 'M'
            cupboard[current_row][current_col] = '*'

        elif cupboard[next_row][next_col] == '@':
            continue

    else:
        print("No more cheese for tonight!")
        break

[print(*data, sep='') for data in cupboard]
