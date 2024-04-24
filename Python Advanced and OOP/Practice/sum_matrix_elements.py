# rows, columns = input().split(', ')
# matrix = []
# total_sum = 0
# for row in range(int(rows)):
#     matrix.append([])
#     elements = list(map(int, input().split(', ')))
#     for column in range(int(columns)):
#         matrix[row].append(elements[column])
#         total_sum += elements[column]
#
# print(total_sum)
# print(matrix)

data = input().split(', ')
rows = int(data[0])
columns = int(data[1])
matrix = []
total_sum = 0

for _ in range(rows):
    numbers = list(map(int, input().split(', ')))
    matrix.append(numbers)
    total_sum += sum(numbers)

print(total_sum)
print(matrix)
