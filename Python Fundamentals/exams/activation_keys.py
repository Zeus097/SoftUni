raw_key = input()

while True:
    command = input()
    if command == 'Generate':
        break

    action = command.split('>>>')
    if action[0] == 'Contains':
        substring = action[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action[0] == 'Flip':
        start_index = int(action[2])
        end_index = int(action[3])
        if action[1] == 'Upper':
            raw_key = raw_key.replace(raw_key[start_index:end_index], raw_key[start_index:end_index].upper())
        elif action[1] == 'Lower':
            raw_key = raw_key.replace(raw_key[start_index:end_index], raw_key[start_index:end_index].lower())
        print(raw_key)

    elif action[0] == 'Slice':
        start_index = int(action[1])
        end_index = int(action[2])
        raw_key = raw_key.replace(raw_key[start_index:end_index], '')
        print(raw_key)

print(f"Your activation key is: {raw_key}")
