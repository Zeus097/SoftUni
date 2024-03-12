text = input()
encrypted_text = ""

for character in text:
    encrypted_message = chr(ord(character) + 3)
    encrypted_text += encrypted_message
print(encrypted_text)
