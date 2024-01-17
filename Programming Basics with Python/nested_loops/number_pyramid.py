number = int(input())
counter = 1
flag = False

for row in range(1, number +1):
    for colum in range(1, row + 1):
        print(counter, end=" ")
        counter += 1

        if counter > number:
            flag = True
            break
    if flag:
        break
    print()