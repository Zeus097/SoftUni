def is_valid(numbers, i, j):
    row1, row2 = int(numbers[0]), int(numbers[2])
    col1, col2 = int(numbers[1]), int(numbers[3])
    if 0 <= row1 < i:
        return True
    if 0 <= row2 < i:
        return True
    if 0 <= col1 < j:
        return True
    if 0 <= col2 < j:
        return True
    else:
        return False


rows, cols = list(map(int, input().split()))
matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] == "swap" and len(command) == 5:
        action = list(map(int, command[1:]))
        if is_valid(action, rows, cols):
            matrix[action[0]][action[1]], matrix[action[2]][action[3]] = matrix[action[2]][action[3]], matrix[action[0]][action[1]]
            for index in range(len(matrix)):
                print(*[x for x in matrix[index]])

        else:
            print("Invalid input!")
            continue

    else:
        print("Invalid input!")
        continue
