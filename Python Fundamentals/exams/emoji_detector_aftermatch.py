import re


def validating_strings(matched_strings):
    valid_strings = []

    for match in matched_strings:
        for current_match in match:
            if current_match:
                valid_strings.append(current_match)
    return valid_strings


def calculating_coolness(valid_emojis, treshold_sum):
    coolest_emojis = []
    total_coolness = 0
    for cool_emoji in valid_emojis:
        for char in cool_emoji[2:len(cool_emoji) - 2]:
            char_number = ord(char)
            total_coolness += char_number
        if total_coolness >= treshold_sum:
            coolest_emojis.append(cool_emoji)
        total_coolness = 0

    return coolest_emojis


def treshold(string):
    treshold_sum = 1
    for char in string:
        if char.isdigit():
            treshold_sum *= int(char)

    return treshold_sum


def print_function(treshold_sum, emoji_number, emojis):
    print(f"Cool threshold: {treshold_sum}")
    print(f"{emoji_number} emojis found in the text. The cool ones are:")
    for emoji in emojis:
        print(emoji)


def main():
    piece_of_string = input()
    pattern = r'([:]{2}[A-Z][a-z]{2,}[:]{2})|([*]{2}[A-Z][a-z]{2,}[*]{2})'
    matches = re.findall(pattern, piece_of_string)

    valid_matches = validating_strings(matches)
    emoji_found_number = len(valid_matches)
    cool_treshold = treshold(piece_of_string)
    cool_emojis = calculating_coolness(valid_matches, cool_treshold)
    print_function(cool_treshold, emoji_found_number, cool_emojis)


if __name__ == '__main__':
    main()
