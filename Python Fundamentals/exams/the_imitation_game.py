message = input()
while True:
    command = input()
    if command == 'Decode':
        break

    instructions = command.split('|')

    if instructions[0] == 'Move':
        number_of_letters = int(instructions[1])
        letters = message[:number_of_letters]
        message = message.replace(letters, '')
        message += letters

    elif instructions[0] == 'Insert':
        index = int(instructions[1])
        value = instructions[2]
        message = message[:index] + value + message[index:]

    elif instructions[0] == 'ChangeAll':
        substring = instructions[1]
        replacement = instructions[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
