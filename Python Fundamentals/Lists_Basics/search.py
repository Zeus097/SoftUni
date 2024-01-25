number = int(input())
word = input()

total_words = []
sorted_words = []

for element in range(number):
    current_string = input()
    total_words.append(current_string)

    if word in current_string:
        sorted_words.append(current_string)

print(total_words)
print(sorted_words)
