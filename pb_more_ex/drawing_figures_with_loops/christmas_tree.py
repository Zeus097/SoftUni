n = int(input())

for i in range(n):
    spaces = " " * (n - i - 1)
    stars = "*" * (i + 1)
    if i == 0:
        print(spaces + "  | ")
    print(spaces + stars + " | " + stars)
    