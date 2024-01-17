number_of_coffees = 0

while True:
    command = input()

    if command == "END":
        break

    if (command not in "coding" and command not in "CODING"
            and command not in "dog" and command not in "DOG"
            and command not in "cat" and command not in "CAT"
            and command not in "movie" and command not in "MOVIE"):
        continue

    if command.islower():
        number_of_coffees += 1
    elif command.isupper():
        number_of_coffees += 2

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)
