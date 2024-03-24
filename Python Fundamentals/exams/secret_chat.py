message_string = input()
while True:
    command = input()
    if command == 'Reveal':
        break

    string_with_instructions = command.split(':|:')

    if string_with_instructions[0] == 'InsertSpace':
        given_index = int(string_with_instructions[1])
        message_string = message_string[:given_index] + ' ' + message_string[given_index:]

    elif string_with_instructions[0] == 'Reverse':
        substring = string_with_instructions[1]
        if substring in message_string:
            message_string = message_string.replace(substring, '', 1)
            substring = substring[::-1]
            message_string += substring
        else:
            print('error')
            continue

    elif string_with_instructions[0] == 'ChangeAll':
        substring = string_with_instructions[1]
        replacement = string_with_instructions[2]
        message_string = message_string.replace(substring, replacement)

    print(message_string)

print(f'You have a new text message: {message_string}')
