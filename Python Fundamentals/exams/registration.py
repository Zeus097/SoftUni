username = input()
while True:
    command = input().split()
    if command[0] == 'Registration':
        break

    if command[0] == 'Letters':
        if command[1] == 'Lower':
            username = username.lower()
        elif command[1] == 'Upper':
            username = username.upper()

        print(username)

    if command[0] == 'Reverse':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            reversed_username = username[start_index:end_index + 1][::-1]
            print(reversed_username)
        else:
            continue

    if command[0] == 'Substring':
        substring = command[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    if command[0] == 'Replace':
        given_char = command[1]
        username = username.replace(given_char, '-')
        print(username)

    if command[0] == 'IsValid':
        given_char = command[1]
        if given_char in username:
            print("Valid username.")
        else:
            print(f"{given_char} must be contained in your username.")
