def square_2x2(matr, row, col):
    return matr[row][col] == matr[row][col + 1] == matr[row + 1][col] == matr[row + 1][col + 1]


rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
square_matrices_number = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        if square_2x2(matrix, i, j):
            square_matrices_number += 1

print(square_matrices_number)
