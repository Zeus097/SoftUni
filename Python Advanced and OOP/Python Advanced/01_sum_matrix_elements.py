rows, cols = list(map(int, input().split(', ')))
matrix = []
sum_numbers = 0

for i in range(rows):
    data = list(map(int, input().split(', ')))
    matrix.append([])
    for j in range(cols):
        matrix[i].append(data[j])
    sum_numbers += sum(data)

print(sum_numbers)
print(matrix)
