string = input()
while True:
    new_string = ''
    command = input()
    if command == 'Done':
        break

    action = command.split()
    if action[0] == 'TakeOdd':
        for index in range(len(string)):
            if index % 2 != 0:
                new_string += string[index]
        string = new_string
        print(new_string)

    elif action[0] == 'Cut':
        current_index = int(action[1])
        length = int(action[2])
        new_string += string[current_index:current_index + length]
        string = string.replace(new_string, '', 1)
        print(string)

    elif action[0] == 'Substitute':
        substring = action[1]
        substitute = action[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {string}")
