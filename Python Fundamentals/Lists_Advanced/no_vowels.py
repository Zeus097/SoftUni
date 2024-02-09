some_text = input()
new_text = [word for word in some_text if word.casefold() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(new_text))
