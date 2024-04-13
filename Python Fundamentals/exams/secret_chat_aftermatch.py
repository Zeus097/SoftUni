def revealing_secret_message(message):
    while True:
        command = input()
        if command == 'Reveal':
            break

        action = command.split(':|:')
        if action[0] == 'InsertSpace':
            index = int(action[1])
            message = message[:index] + ' ' + message[index:]

        elif action[0] == 'Reverse':
            substring = action[1]
            if substring in message:
                message = message.replace(substring, '', 1)
                message += substring[::-1]
            else:
                print("error")
                continue

        elif action[0] == 'ChangeAll':
            substring = action[1]
            replacement = action[2]
            if substring in message:
                message = message.replace(substring, replacement)

        print(message)

    return f"You have a new text message: {message}"


secret_message = input()
revealed_message = revealing_secret_message(secret_message)
print(revealed_message)
