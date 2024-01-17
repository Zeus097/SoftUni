word = input().lower()

total_count = 0
search_for = ["sand", "water", "fish", "sun"]

for list_index in range(len(search_for)):
    counter = word.count(search_for[list_index])
    if counter > 0:
        total_count += counter
print(total_count)