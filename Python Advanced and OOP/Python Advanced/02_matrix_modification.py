def validation(mtr, r, c):
    return int(r) in range(0, len(mtr)) and int(c) in range(0, len(mtr))


matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

while True:
    command = input()
    if command == 'END':
        [print(*el) for el in matrix]
        break

    command_line, row, col, value = command.split()
    if not validation(matrix, row, col):
        print("Invalid coordinates")
    else:
        if command_line == 'Add':
            matrix[int(row)][int(col)] += int(value)
        elif command_line == 'Subtract':
            matrix[int(row)][int(col)] -= int(value)
