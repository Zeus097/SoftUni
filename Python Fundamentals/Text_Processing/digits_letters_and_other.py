string = input()
digits_found = ""
letters_found = ""
other_characters_found = ""

for char in string:
    if char.isdigit():
        digits_found += char
    elif char.isalpha():
        letters_found += char
    else:
        other_characters_found += char

print(digits_found)
print(letters_found)
print(other_characters_found)
