string = input()
while True:
    command = input()
    if command == 'End':
        break

    action = command.split()
    if action[0] == 'Translate':
        char = action[1]
        replacement = action[2]
        string = string.replace(char, replacement)
        print(string)

    elif action[0] == 'Includes':
        substring = action[1]
        if substring in string:
            print(True)
        else:
            print(False)

    elif action[0] == 'Start':
        substring = action[1]
        if string.startswith(substring):
            print(True)
        else:
            print(False)

    elif action[0] == 'Lowercase':
        string = string.lower()
        print(string)

    elif action[0] == 'FindIndex':
        char = action[1]
        print(string.rindex(char))

    elif action[0] == 'Remove':
        start_index = int(action[1])
        count = int(action[2])
        string = string[:start_index] + string[start_index + count:]
        print(string)
