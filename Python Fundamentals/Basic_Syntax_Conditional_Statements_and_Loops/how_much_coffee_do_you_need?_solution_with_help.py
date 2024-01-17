number_of_coffees = 0

while True:
    command = input()

    if command == "END":
        break

    if (command.lower() in "coding"
            or command.lower() in "dog" or command.lower() in "cat"
            or command.lower() in "movie"):
        if command.islower():
            number_of_coffees += 1
        elif command.isupper():
            number_of_coffees += 2


if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)
