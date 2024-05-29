n = int(input())
matrix = []
bunnyes = []
for i in range(n):
    matrix.append([x for x in input().split()])
    for j in range(n):
        if matrix[i][j] == 'B':
            bunnyes = [i, j]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

max_direction = ''
eggs_matrix = []
max_eggs = -float('inf')

for direction, position in directions.items():
    current_eggs = 0
    current_direction_matrix = []
    row = bunnyes[0] + position[0]
    col = bunnyes[1] + position[1]

    while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        if matrix[row][col] == 'X':
            break
        current_eggs += int(matrix[row][col])
        current_direction_matrix.append([row, col])
        row += position[0]
        col += position[1]

    if current_eggs > max_eggs and current_direction_matrix:
        max_eggs = current_eggs
        eggs_matrix = current_direction_matrix
        max_direction = direction

print(max_direction)
[print(row, sep=' ') for row in eggs_matrix]
print(max_eggs)
