rows = int(input())
matrix = []

for i in range(rows):
    data = [char for char in input()]
    matrix.append(data)

symbol = input()
for i in range(rows):
    if symbol is None:
        break
    for j in range(rows):
        if symbol == matrix[i][j]:
            print(f"({i}, {j})")
            symbol = None
            break

if symbol is not None:
    print(f"{symbol} does not occur in the matrix")
