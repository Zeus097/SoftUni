# words = input().split()
# words_sequence = {}
# for index in range(len(words)):
#     word = words[index].lower()
#     if word in words_sequence.keys():
#         words_sequence[word].append(word)
#     else:
#         words_sequence[word] = []
#         words_sequence[word].append(word)
#
# for key, value in words_sequence.items():
#     if len(value) % 2 != 0:
#         print(key, end=" ")

words = input().split()
dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
