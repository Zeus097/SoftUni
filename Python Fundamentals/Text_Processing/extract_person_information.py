number_of_lines = int(input())

for index in range(number_of_lines):
    string = input()
    name = ""
    age = ""
    combination_found = False
    for current_index in range(len(string)):
        if string[current_index].startswith("@"):
            for character in range(current_index, len(string)):
                current_index += 1
                if string[current_index] == "|":
                    break
                name += string[current_index]
        elif string[current_index].startswith("#"):
            for digit in range(current_index, len(string)):
                current_index += 1
                if string[current_index] == "*":
                    combination_found = True
                    break
                age += string[current_index]
    if combination_found:
        print(f"{name} is {int(age)} years old.")
