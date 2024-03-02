list_of_characters = input().split(", ")
dict_of_characters = {}
for index in list_of_characters:
    dict_of_characters[index] = ord(index)

print(dict_of_characters)
