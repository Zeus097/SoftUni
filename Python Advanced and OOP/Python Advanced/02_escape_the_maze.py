def printing_maze(current_state):
    return [print(''.join(state)) for state in current_state]


n = int(input())
maze = []
health = 100
traveler_position = None

for row_index in range(n):
    maze.append(list(input()))
    if 'P' in maze[row_index]:
        col_index = maze[row_index].index('P')
        traveler_position = (row_index, col_index)

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while health > 0:
    direction = input()
    current_row = traveler_position[0]
    current_col = traveler_position[1]

    next_row = current_row + directions[direction][0]
    next_col = current_col + directions[direction][1]

    if 0 <= next_row < len(maze) and 0 <= next_col < len(maze):

        if maze[next_row][next_col] == 'M':

            maze[next_row][next_col] = 'P'
            maze[current_row][current_col] = '-'
            health -= 40
            if health <= 0:
                health = 0
                print("Player is dead. Maze over!")
                print(f"Player's health: {health} units")
                printing_maze(maze)
                break

        elif maze[next_row][next_col] == 'H':

            maze[next_row][next_col] = 'P'
            maze[current_row][current_col] = '-'
            health = min(health + 15, 100)

        elif maze[next_row][next_col] == 'X':

            maze[next_row][next_col] = 'P'
            maze[current_row][current_col] = '-'
            print("Player escaped the maze. Danger passed!")
            print(f"Player's health: {health} units")
            printing_maze(maze)
            break
        else:
            maze[next_row][next_col] = 'P'
            maze[current_row][current_col] = '-'

        traveler_position = (next_row, next_col)
    else:
        continue
