rows = int(input())

# Upper half of the diamond
for i in range(1, rows, 2):  # Loop for odd values of i
    spaces = (rows - i) // 2
    for j in range(spaces):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(spaces):
        print(" ", end="")
    print()

# Lower half of the diamond
for i in range(rows, 0, -2):  # Loop for even values of i
    spaces = (rows - i) // 2
    for j in range(spaces):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(spaces):
        print(" ", end="")
    print()


# this diamond is made of parts of triangles
#
# number = 5
# for i in range(number - 1):
#     for j in range(i, number):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# for i in range(number):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, number - 1):
#         print("*", end=" ")
#     for j in range(i, number):
#         print("*", end=" ")
#     print()