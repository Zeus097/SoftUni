n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-i - 1] for i in range(n)]
difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)
