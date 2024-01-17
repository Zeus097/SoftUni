sorting_hat = ""
forbidden_name = False

while True:
    command = input()

    if command == "Welcome!":
        break

    name = command
    if name == "Voldemort":
        sorting_hat = "You must not speak of that name!"
        forbidden_name = True
        break

    if len(name) < 5:
        sorting_hat = f"{name} goes to Gryffindor."
    elif len(name) == 5:
        sorting_hat = f"{name} goes to Slytherin."
    elif len(name) == 6:
        sorting_hat = f"{name} goes to Ravenclaw."
    else:
        sorting_hat = f"{name} goes to Hufflepuff."

    print(sorting_hat)
if forbidden_name:
    print(sorting_hat)
else:
    print("Welcome to Hogwarts.")
