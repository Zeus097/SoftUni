list_of_banned_words = input().split(", ")
text = input()

for word in list_of_banned_words:
    text = text.replace(word, len(word) * "*")
print(text)
