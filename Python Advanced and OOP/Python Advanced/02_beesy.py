# Total 90 / 100 in JUDGE

def printing_matrix(matrix):
    return [print(*line, sep='') for line in matrix]


n = int(input())
bee_position = None
field = []

for rows_index in range(n):
    data = list(input().strip())
    field.append(data)
    if 'B' in data:
        col_index = data.index('B')
        bee_position = (rows_index, col_index)

bee_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

collected_nectar = 0
initial_health = 15
restored_energy = True

while True:
    if initial_health == 0:
        if collected_nectar >= 30 and restored_energy:
            restored_energy = False
            initial_health += collected_nectar - 30
            collected_nectar = 30
            continue
        print("This is the end! Beesy ran out of energy.")
        break

    command = input()
    current_row = bee_position[0]
    current_col = bee_position[1]

    next_row = current_row + bee_moves[command][0]
    next_col = current_col + bee_moves[command][1]

    if not (0 <= current_row + bee_moves[command][0] < len(bee_moves) and
            0 <= current_col + bee_moves[command][1] < len(field)):
        next_row = (next_row + len(field)) % len(field)
        next_col = (next_col + len(field)) % len(field)

    initial_health -= 1

    if field[next_row][next_col] == 'H':
        bee_position = (next_row, next_col)
        field[next_row][next_col] = 'B'
        field[current_row][current_col] = '-'
        if collected_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {initial_health}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    elif field[next_row][next_col].isdigit():
        flower = field[next_row][next_col]
        collected_nectar += int(flower)

    bee_position = (next_row, next_col)
    field[next_row][next_col] = 'B'
    field[current_row][current_col] = '-'

printing_matrix(field)
