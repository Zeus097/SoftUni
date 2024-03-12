string = input()
new_string = ""
strenght = 0

for index in range(len(string)):
    if strenght > 0 and string[index] != '>':
        strenght -= 1

    elif string[index] == '>':
        new_string += string[index]
        strenght += int(string[index + 1])

    else:
        new_string += string[index]
print(new_string)
