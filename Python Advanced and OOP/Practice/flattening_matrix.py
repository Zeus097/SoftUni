rows = int(input())
matrix = []

for row in range(rows):
    elements = list(map(int, input().split(', ')))
    for element in range(len(elements)):
        matrix.append(elements[element])

print(matrix)
