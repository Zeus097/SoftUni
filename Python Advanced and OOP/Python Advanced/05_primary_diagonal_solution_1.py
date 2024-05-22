rows = int(input())
matrix = []
diagonal_sum = 0
counter = 0

for i in range(rows):
    data = list(map(int, input().split()))
    matrix.append(data)
    for j in range(rows):
        diagonal_sum += matrix[i][counter]
        counter += 1
        break

print(diagonal_sum)
