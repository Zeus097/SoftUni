presents_count = int(input())
n = int(input())
matrix = []
santa = []
nice_kids_count = 0
total_nice_kids = 0

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == 'S':
            santa = [i, j]
            matrix[i][j] = '-'
        elif matrix[i][j] == 'V':
            nice_kids_count += 1
            total_nice_kids += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
while True:
    command = input()
    if command == 'Christmas morning':
        matrix[santa[0]][santa[1]] = 'S'
        break

    row = santa[0] + directions[command][0]
    col = santa[1] + directions[command][1]

    if 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'V' and presents_count > 0:
            presents_count -= 1
            nice_kids_count -= 1
            santa = [row, col]
            matrix[row][col] = '-'

        elif matrix[row][col] == 'X':
            santa = [row, col]
            matrix[row][col] = '-'

        elif matrix[row][col] == 'C':
            santa = [row, col]
            matrix[row][col] = '-'

            if matrix[row - 1][col] != '-' and presents_count > 0:  # --> Up
                presents_count -= 1
                if matrix[row - 1][col] == 'V':
                    nice_kids_count -= 1
                    matrix[row - 1][col] = '-'
                else:
                    matrix[row - 1][col] = '-'

            if matrix[row + 1][col] != '-' and presents_count > 0:  # --> Down
                presents_count -= 1
                if matrix[row + 1][col] == 'V':
                    nice_kids_count -= 1
                    matrix[row + 1][col] = '-'
                else:
                    matrix[row + 1][col] = '-'

            if matrix[row][col - 1] != '-' and presents_count > 0:  # --> Left
                presents_count -= 1
                if matrix[row][col - 1] == 'V':
                    nice_kids_count -= 1
                    matrix[row][col - 1] = '-'
                else:
                    matrix[row][col - 1] = '-'

            if matrix[row][col + 1] != '-' and presents_count > 0:  # --> Right
                presents_count -= 1
                if matrix[row][col + 1] == 'V':
                    nice_kids_count -= 1
                    matrix[row][col + 1] = '-'
                else:
                    matrix[row][col + 1] = '-'

        else:
            santa = [row, col]

        if presents_count == 0:
            matrix[row][col] = 'S'
            break

if presents_count == 0 and nice_kids_count > 0:
    print("Santa ran out of presents!")
[print(*neighbourhood, sep=' ') for neighbourhood in matrix]
if nice_kids_count == 0:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")
