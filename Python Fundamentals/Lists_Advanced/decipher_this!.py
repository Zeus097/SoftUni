def converting_characters(secret_message):
    integer_as_string = ""
    string = ""
    converted_characters = []

    for character in secret_message:
        if len(integer_as_string) != 0:
            converted_integer = chr(int(integer_as_string))

            while integer_as_string:
                new_word = converted_integer + string
                converted_characters.append(new_word)
                integer_as_string = ""
                string = ""

        for char in character:
            if char.isdigit():
                integer_as_string += char
            else:
                string += char

    converted_integer = chr(int(integer_as_string))
    new_word = converted_integer + string
    converted_characters.append(new_word)


    return converted_characters


def swapping_letters(converted_text):
    deciphered_message = []
    for word in converted_text:
        if len(word) < 3:
            decipher = "".join([word])
        else:
            decipher = "".join([word[0] + word[-1] + word[2:-1] + word[1]])
        deciphered_message.append(decipher)


    return " ".join(deciphered_message)



secret_message = input().split()

converted_text = converting_characters(secret_message)
deciphered_text = swapping_letters(converted_text)
print(deciphered_text)
