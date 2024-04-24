rows = int(input())
matrix = []
for _ in range(rows):
    elements = list(map(int, input().split(', ')))
    matrix.append([element for element in elements if element % 2 == 0])
print(matrix)
