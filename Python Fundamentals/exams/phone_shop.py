list_of_phones = input().split(", ")
command = input()

while True:
    if command == "End":
        break

    command = command.split(" - ")
    if command[0] == "Add":
        current_phone = command[1]
        if current_phone not in list_of_phones:
            list_of_phones.append(current_phone)
    elif command[0] == "Remove":
        current_phone = command[1]
        if current_phone in list_of_phones:
            list_of_phones.remove(current_phone)
    elif command[0] == "Bonus phone":
        new_phones = command[1].split(":")
        old_phone = new_phones[0]
        new_phone = new_phones[1]
        if old_phone in list_of_phones:
            old_phone_index = list_of_phones.index(old_phone)
            list_of_phones.insert(old_phone_index + 1, new_phone)
    elif command[0] == "Last":
        current_phone = command[1]
        if current_phone in list_of_phones:
            list_of_phones.remove(current_phone)
            list_of_phones.append(current_phone)

    command = input()

new_phones = ", ".join(list_of_phones)
print(new_phones)
