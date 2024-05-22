rows, columns = map(int, input().split(', '))

matrix = []
cols_sum = 0
for i in range(rows):
    matrix.append(list(map(int, input().split())))

for i in range(columns):
    cols_sum = 0
    for j in range(rows):
        cols_sum += matrix[j][i]
    print(cols_sum)
