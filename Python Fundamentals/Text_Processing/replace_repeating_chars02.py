text_sequence = input()
new_text = ""
current_char = ""

for character in text_sequence:
    if character != current_char:
        current_char = character
        new_text += current_char

print(new_text)