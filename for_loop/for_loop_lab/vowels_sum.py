text = input()
x = 0

for letter in range(0, len(text)):
    if text[letter] == "a":
        x += 1
    elif text[letter] == "e":
        x += 2
    elif text[letter] == "i":
        x += 3
    elif text[letter] == "o":
        x += 4
    elif text[letter] == "u":
        x += 5
print(x)