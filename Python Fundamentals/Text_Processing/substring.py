string = input()
modified_string = input()

while string in modified_string:
    modified_string = modified_string.replace(string, '')
print(modified_string)
