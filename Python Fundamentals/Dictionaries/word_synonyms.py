word_counter = int(input())
dictionary = {}

for _ in range(word_counter):
    word = input()
    synonyms = input()

    if word not in dictionary:
        dictionary[word] = []

    dictionary[word].append(synonyms)

for key, value in dictionary.items():
    synonyms_value = ", ".join(value)
    print(f"{key} - {synonyms_value}")
