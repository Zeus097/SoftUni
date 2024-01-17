number = int(input())

for i in range(1, number + 1, 1):
    for j in range(0, i, 1):
        print("*", end="")
    print()


# second solution for the same pattern

# number = int(input())
#
# for i in range(number):
#     for j in range(i + 1):
#         print("*", end="")
#     print()
