def printing_matrix(field):
    return [print(''.join(air_field)) for air_field in field]


n = int(input())
matrix = []
armor = 300
enemyes = 4
jetfire_position = None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row_index in range(n):
    data = list(input())
    matrix.append(data)
    if "J" in data:
        col_index = data.index("J")
        jetfire_position = (row_index, col_index)

while enemyes or armor == 0:
    command = input()

    current_row_index = jetfire_position[0]
    current_col_index = jetfire_position[1]

    next_row_index = current_row_index + directions[command][0]
    next_col_index = current_col_index + directions[command][1]

    run_position = matrix[next_row_index][next_col_index]

    if run_position == "-":
        jetfire_position = (next_row_index, next_col_index)
        matrix[next_row_index][next_col_index] = "J"
        matrix[current_row_index][current_col_index] = "-"

    elif run_position == "E":
        jetfire_position = (next_row_index, next_col_index)
        matrix[next_row_index][next_col_index] = "J"
        matrix[current_row_index][current_col_index] = "-"
        enemyes -= 1
        if enemyes == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            printing_matrix(matrix)
            break

        armor -= 100
        if armor == 0:
            row = jetfire_position[0]
            col = jetfire_position[1]
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
            printing_matrix(matrix)
            break

    elif run_position == "R":
        armor = 300
        jetfire_position = (next_row_index, next_col_index)
        matrix[next_row_index][next_col_index] = "J"
        matrix[current_row_index][current_col_index] = "-"
