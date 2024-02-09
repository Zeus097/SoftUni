number_of_wagons = int(input())
train = [0] * number_of_wagons
while True:
    command = input().split()

    if command[0] == "End":
        print(train)
        break

    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people
