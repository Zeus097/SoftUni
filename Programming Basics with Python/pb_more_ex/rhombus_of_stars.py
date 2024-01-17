number = int(input())

# Generate the top part
for row in range(1, number + 1):
    print(" " * (number - row) + "* " * (row - 1) + "*")

# Generate the bottom part
for row in range(1, number):
    print(" " * row + "* " * (number - row - 1) + "*")
