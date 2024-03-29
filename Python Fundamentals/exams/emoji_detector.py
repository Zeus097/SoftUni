import re


piece_of_string = input()
pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'
matches = re.finditer(pattern, piece_of_string)
valid_emojis = []
cool_threshold_sum = 1
for match in matches:
    current_emoji = ''
    current_emoji += match.group(1) + match.group(2) + match.group(1)
    valid_emojis.append(current_emoji)

for letter in piece_of_string:
    if letter.isdigit():
        cool_threshold_sum *= int(letter)

print(f"Cool threshold: {cool_threshold_sum}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
for emoji in valid_emojis:
    coolnes = 0
    for char in emoji[2:len(emoji) - 2]:
        coolnes += ord(char)
    if coolnes > cool_threshold_sum:
        print(f"{emoji} ")
