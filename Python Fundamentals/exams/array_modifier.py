values = list(map(int, input().split()))
command = input().split()


while True:
    command_as_string = command[0]
    if command_as_string == "end":
        break

    if command_as_string != "decrease":
        first_command_number = int(command[1])
        second_command_number = int(command[2])

        if command_as_string == "swap":
            values[first_command_number], values[second_command_number] =\
                values[second_command_number], values[first_command_number]

        elif command_as_string == "multiply":
            values[first_command_number] *= values[second_command_number]

    if command_as_string == "decrease":
        modified_numbers = []
        for number in values:
            number -= 1
            modified_numbers.append(number)
        values.clear()
        for number in modified_numbers:
            values.append(number)

    command = input().split()

modified_numbers = ", ".join(map(str, values))
print(modified_numbers)
