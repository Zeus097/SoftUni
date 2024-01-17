figure = "*"
number = 10
flag = False

for row in range(number):
    for column in range(number):
        print(figure, end="")

        if number > 10:
            flag = True
            break

    if flag:
        break
    print()