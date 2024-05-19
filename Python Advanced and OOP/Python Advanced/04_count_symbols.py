text = input()
collection = {}

for char in range(len(text)):
    current_char = text[char]
    if current_char not in collection:
        collection[current_char] = set()
    collection[current_char].add(text.count(current_char))

sorted_collection = sorted(collection.items())
for letter, count in sorted_collection:
    letters_count = ''.join([str(current_count) for current_count in count])
    print(f"{letter}: {letters_count} time/s")
