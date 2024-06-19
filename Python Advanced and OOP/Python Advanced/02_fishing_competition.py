matrix_size = int(input())
fishing_area = []
vessel_position = None

for row_index in range(matrix_size):
    fishing_area.append(list(input()))
    if 'S' in fishing_area[row_index]:
        col_index = fishing_area[row_index].index('S')
        vessel_position = (row_index, col_index)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

FISH_NEEDED = 20
collected_fish = 0
command = input()
while command != 'collect the nets':
    current_row = vessel_position[0]
    current_col = vessel_position[1]

    if (0 <= current_row + directions[command][0] < len(fishing_area) and
            0 <= current_col + directions[command][1] < len(fishing_area)):
        next_row = current_row + directions[command][0]
        next_col = current_col + directions[command][1]

    else:
        next_row = current_row + directions[command][0]
        next_col = current_col + directions[command][1]

        next_row = (next_row + len(fishing_area)) % len(fishing_area)
        next_col = (next_col + len(fishing_area)) % len(fishing_area)

    if fishing_area[next_row][next_col].isdigit():
        collected_fish += int(fishing_area[next_row][next_col])
        vessel_position = (next_row, next_col)
        fishing_area[current_row][current_col] = '-'
        fishing_area[next_row][next_col] = 'S'

    elif fishing_area[next_row][next_col] == '-':
        vessel_position = (next_row, next_col)
        fishing_area[next_row][next_col] = 'S'
        fishing_area[current_row][current_col] = '-'

    elif fishing_area[next_row][next_col] == 'W':
        vessel_position = (next_row, next_col)
        collected_fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{vessel_position[0]},{vessel_position[1]}]")
        exit()

    command = input()

if collected_fish >= FISH_NEEDED:
    print("Success! You managed to reach the quota!")
else:
    fish_needed = FISH_NEEDED - collected_fish
    print(f"You didn't catch enough fish and didn't reach the quota! You need {fish_needed} tons of fish more.")

if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print(*field, sep='') for field in fishing_area]
