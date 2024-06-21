def printing_matrix(matrix):
    return [print(*line, sep='') for line in matrix]


n = int(input())
board = []
gambles_position = None
amount = 100

for row in range(n):
    board.append(list(input()))
    if 'G' in board[row]:
        col = board[row].index('G')
        gambles_position = (row, col)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input()
while command != 'end':
    current_row = gambles_position[0]
    current_col = gambles_position[1]

    next_row = current_row + directions[command][0]
    next_col = current_col + directions[command][1]

    if not (0 <= next_row < len(board) and 0 <= next_col < len(board)):
        print("Game over! You lost everything!")
        exit()

    else:

        if board[next_row][next_col] == '-':
            board[next_row][next_col] = 'G'
            board[current_row][current_col] = '-'
            gambles_position = (next_row, next_col)

        elif board[next_row][next_col] == 'W':
            amount += 100
            board[next_row][next_col] = 'G'
            board[current_row][current_col] = '-'
            gambles_position = (next_row, next_col)

        elif board[next_row][next_col] == 'P':
            amount -= 200
            board[next_row][next_col] = 'G'
            board[current_row][current_col] = '-'
            gambles_position = (next_row, next_col)
            if amount <= 0:
                print("Game over! You lost everything!")
                exit()

        elif board[next_row][next_col] == 'J':
            amount += 100000
            board[next_row][next_col] = 'G'
            board[current_row][current_col] = '-'
            gambles_position = (next_row, next_col)

            print(f"You win the Jackpot!\nEnd of the game. Total amount: {amount}$")
            printing_matrix(board)
            exit()

    command = input()

print(f"End of the game. Total amount: {amount}$")
printing_matrix(board)
