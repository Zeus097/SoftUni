string_sequence = input()
new_string = ""
current_string = ""

for index in range(len(string_sequence)):
    if index == 0:
        current_string += string_sequence[index]
        new_string += current_string

    if string_sequence[index] != current_string:
        new_string += string_sequence[index]
        current_string = string_sequence[index]

print(new_string)
