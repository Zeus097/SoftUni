def square_max_sum(mtrx, i, j):
    square = [
                    [mtrx[i][j], mtrx[i][j + 1], mtrx[i][j + 2]],
                    [mtrx[i + 1][j], mtrx[i + 1][j + 1], mtrx[i + 1][j + 2]],
                    [mtrx[i + 2][j], mtrx[i + 2][j + 1], mtrx[i + 2][j + 2]]
                    ]
    return square


rows, columns = list(map(int, input().split()))
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = - float("inf")
max_square = []
for row in range(rows - 2):
    for col in range(columns - 2):
        current_square = square_max_sum(matrix, row, col)
        current_sum = 0

        for collection in range(len(current_square)):
            current_sum += sum(current_square[collection])

        if current_sum > max_sum:
            max_sum = current_sum

            if len(max_square) != 0:
                max_square.clear()
            max_square = current_square

print(f"Sum = {max_sum}")
for current_row in range(len(max_square)):
    for current_column in range(len(max_square)):
        if current_column == len(max_square) - 1:
            print(max_square[current_row][current_column])
        else:
            print(max_square[current_row][current_column], end=" ")
