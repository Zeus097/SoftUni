array_of_integers = list(map(int, input().split()))
command = input().split()

while True:
    if command[0] == "end":
        break
    action = command[0]
    if action == "swap":
        index_1, index_2 = int(command[1]), int(command[2])
        array_of_integers[index_1], array_of_integers[index_2] =\
            array_of_integers[index_2], array_of_integers[index_1]
    elif action == "multiply":
        index_1, index_2 = int(command[1]), int(command[2])
        array_of_integers[index_1] *= array_of_integers[index_2]
    elif action == "decrease":
        array_of_integers = [array - 1 for array in array_of_integers]
    command = input().split()
print(*array_of_integers, sep=", ")
