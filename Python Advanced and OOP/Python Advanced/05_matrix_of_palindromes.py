rows, columns = list(map(int, input().split()))
matrix = []
outer_index = 0

for i in range(outer_index, rows):
    matrix.append([])
    for j in range(i, columns + i):
        matrix[i].append(chr(97 + i) + chr(97 + j) + chr(97 + i))
    outer_index += 1


for row in range(rows):
    for col in range(columns):
        if col == columns - 1:
            print(matrix[row][col])
        else:
            print(matrix[row][col], end=' ')
