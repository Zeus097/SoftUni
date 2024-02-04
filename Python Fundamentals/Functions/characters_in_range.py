def characters_in_range(first_string, second_string):
    combination = ""
    for char in range(ord(first_string) + 1, ord(second_string)):
        combination += chr(char) + " "
    return combination

first_character = input()
second_character = input()
print(characters_in_range(first_character, second_character))
