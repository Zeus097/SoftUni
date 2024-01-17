word = input()

upper_case_index = []
for char in range(len(word)):
    if word[char].isupper():
        upper_case_index.append(char)

print(upper_case_index)