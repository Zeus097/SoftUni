command = input()
phonebook = {}

while "-" in command:
    name_and_number = command.split("-")
    name, number = name_and_number[0], name_and_number[1]

    phonebook[name] = number
    command = input()

num = int(command)
for _ in range(num):
    current_name = input()
    if current_name not in phonebook:
        print(f"Contact {current_name} does not exist.")
    else:
        print(f"{current_name} -> {phonebook[current_name]}")
