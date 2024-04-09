def modifying_list(integers):
    while True:
        command = input()
        if command == 'end':
            break

        action = command.split()
        if action[0] == 'swap':
            first_index = int(action[1])
            second_index = int(action[2])
            integers[first_index], integers[second_index] = integers[second_index], integers[first_index]

        elif action[0] == 'multiply':
            first_index = int(action[1])
            second_index = int(action[2])
            integers[first_index] *= integers[second_index]

        elif action[0] == 'decrease':
            integers = [number - 1 for number in integers]

    return ', '.join(map(str, integers))


list_with_numbers = list(map(int, input().split()))
modified_list = modifying_list(list_with_numbers)
print(modified_list)
