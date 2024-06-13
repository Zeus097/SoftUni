import re


with open('words.txt', 'r') as file:
    words = [x for x in file.read().split()]

word_count = {}
with open('text.txt') as file:
    text = file.readlines()
    for word in words:
        word_count[word] = 0
        pattern = fr'\b{word}\b'
        for index in range(len(text)):
            result = re.findall(pattern, text[index], re.IGNORECASE)
            if result:
                word_count[word] += len(result)

with open('output.txt', 'w') as file:
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        file.write(f'{word} - {count}\n')
