def activating_key(key):
    while True:
        command = input()
        if command == 'Generate':
            break

        instruction = command.split('>>>')
        if instruction[0] == 'Contains':
            substring = instruction[1]
            if substring in key:
                print(f"{key} contains {substring}")
            else:
                print("Substring not found!")

        elif instruction[0] == 'Flip':
            case_command = instruction[1]
            start_index, end_index = int(instruction[2]), int(instruction[3])
            if case_command == 'Upper':
                key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
            elif case_command == 'Lower':
                key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
            print(key)

        elif instruction[0] == 'Slice':
            start_index, end_index = int(instruction[1]), int(instruction[2])
            key = key[:start_index] + key[end_index:]
            print(key)

    return f"Your activation key is: {key}"


raw_activation_key = input()
generated_key = activating_key(raw_activation_key)
print(generated_key)
