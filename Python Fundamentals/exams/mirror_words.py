import re

text = input()
found_words = []
mirror_words = []
pattern = r'[@]([A-Za-z]{3,})[@]{2}([A-Za-z]{3,})[@]|[#]([A-Za-z]{3,})[#]{2}([A-Za-z]{3,})[#]'
match = re.findall(pattern, text)
for index in range(len(match)):
    for word in match[index]:
        if word != '':
            found_words.append(word)

for index in range(len(found_words)):
    word = found_words[index]
    if index + 1 >= len(found_words):
        break
    mirror_word = found_words[index + 1]
    if word == mirror_word[::-1]:
        mirror_words.append(word)
        mirror_words.append(mirror_word)

found_pairs = len(found_words) // 2


if found_pairs == 0:
    print("No word pairs found!")

if found_pairs > 0:
    print(f"{found_pairs} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")

if len(mirror_words) > 0:
    print("The mirror words are:")

    for index in range(0, len(mirror_words), 2):
        if index + 1 >= len(mirror_words):
            break

        first_word = mirror_words[index]
        second_word = mirror_words[index + 1]

        end_index = len(mirror_words)
        if second_word == mirror_words[-1]:
            print(f"{first_word} <=> {second_word}")
        else:
            print(f"{first_word} <=> {second_word}", end=", ")
