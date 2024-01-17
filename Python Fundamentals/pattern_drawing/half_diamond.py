number = 5

for i in range(number):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(number):
    for j in range(i, number):
        print("*", end=" ")
    print()
