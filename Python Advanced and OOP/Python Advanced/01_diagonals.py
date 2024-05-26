rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for i in range(rows)]

primary_diagonals = [matrix[i][i] for i in range(rows)]


secondary_diagonals = [matrix[i][- i - 1] for i in range(rows)]


print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonals])}. Sum: {sum(primary_diagonals)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonals])}. Sum: {sum(secondary_diagonals)}")
