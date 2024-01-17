# Draw the top part
number = int(input())


print("+", end=" ")
for _ in range(number - 2):
    print("- ", end="")
print("+")

# Draw the middle part
for _ in range(number - 2):
    print("|", end=" ")
    for _ in range(number - 2):
        print("- ", end="")
    print("|")

# Draw the bottom part
print("+", end=" ")
for _ in range(number - 2):
    print("- ", end="")
print("+")


