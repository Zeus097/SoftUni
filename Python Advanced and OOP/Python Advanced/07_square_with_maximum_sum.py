from math import inf

rows, columns = map(int, input().split(', '))
matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split(', '))))

largest_sub_matrix = -inf
needed_sub_matrix = ''
for row in range(rows - 1):
    for col in range(columns - 1):
        top_left = matrix[row][col]
        top_right = matrix[row][col + 1]
        bottom_left = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]

        current_sub_matrix_sum = top_left + top_right + bottom_left + bottom_right
        if current_sub_matrix_sum > largest_sub_matrix:
            largest_sub_matrix = current_sub_matrix_sum

            needed_sub_matrix = f"{top_left} {top_right}\n{bottom_left} {bottom_right}"

print(needed_sub_matrix)
print(largest_sub_matrix)
