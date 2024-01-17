number = 5

for i in range(number):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, number - 1):
        print("*", end=" ")
    for j in range(i, number):
        print("*", end=" ")
    print()


# same but it is next to left side
#
# number = 5
#
# for i in range(number):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i, number - 1):
#         print("*", end=" ")
#     for j in range(i, number):
#         print("*", end=" ")
#     print()
