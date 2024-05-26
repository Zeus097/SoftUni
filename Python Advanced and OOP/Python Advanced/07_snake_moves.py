from collections import deque


r, c = list(map(int, input().split()))
data = deque(input())
matrix = []

for row in range(r):
    matrix.append([''] * c)
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = data[0]
        else:
            matrix[row][-1-col] = data[0]
        data.rotate(-1)

[print(*row, sep='') for row in matrix]
