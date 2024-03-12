char_combination = input().split()
total_sum = 0

for current_char in char_combination:
    first_letter = current_char[0]
    last_letter = current_char[-1]
    current_number = int(current_char[1: len(current_char) - 1])
    if first_letter.isupper():
        letter_position = ord(first_letter) - 64
        total_sum += current_number / letter_position
    elif first_letter.islower():
        letter_position = ord(first_letter) - 96
        total_sum += current_number * letter_position

    if last_letter.isupper():
        letter_position = ord(last_letter) - 64
        total_sum -= letter_position
    elif last_letter.islower():
        letter_position = ord(last_letter) - 96
        total_sum += letter_position

print(f"{total_sum:.2f}")
