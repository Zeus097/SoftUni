figure = "$"
number = int(input())
counter = 0
flag = False

for row in range(1, number + 1):
    counter += 1
    for column in range(1, row + 1):
        print(figure, end=" ")

        if counter > number:
            flag = True
            break

    if flag:
        break
    print()