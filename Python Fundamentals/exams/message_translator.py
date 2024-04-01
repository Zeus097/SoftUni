import re


number_of_strings = int(input())
matched_word = ''
matched_string = ''
translated_string = []
for index in range(number_of_strings):
    current_string = input()
    pattern = r'[!]([A-Z][a-z]+)[!]:\[([a-zA-Z]{8,})\]'
    matches = re.findall(pattern, current_string)
    if matches:
        matched_word = matches[0][0]
        matched_string = matches[0][1]
        for char in matched_string:
            translated_string.append(str(ord(char)))
        print(f"{matched_word}: {' '.join(translated_string)}")

    else:
        print("The message is invalid")




