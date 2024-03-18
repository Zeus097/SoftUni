import re

sentence = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
repetition = re.findall(pattern, sentence, re.IGNORECASE)
print(len(repetition))
