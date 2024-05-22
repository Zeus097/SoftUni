rows = int(input())
matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append([number for number in data if number % 2 == 0])

print(matrix)
