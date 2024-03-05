characters = input().split()
dictionary = {}

for char in characters:
    for letter in char:
        if letter not in dictionary:
            dictionary[letter] = 0
        dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
