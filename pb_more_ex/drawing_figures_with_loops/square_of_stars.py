figure = "*"
number = int(input())
counter = 0
flag = False

for row in range(number):
    counter += 1
    for column in range(number):
        print(figure, end=" ")

        if counter > number:
            flag = True
            break

    if flag:
        break
    print()
