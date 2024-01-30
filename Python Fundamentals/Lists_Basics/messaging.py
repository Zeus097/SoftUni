numbers_sequence = input().split()
message_string = input()
list_of_integers = []

for number in numbers_sequence:
    list_of_integers.append(int(number))

message = []

for number in list_of_integers:
    # Calculate the sum of digits of the current number
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)

    # If the index is greater, continue counting from the beginning
    digit_sum %= len(message_string)

    # Add the character
    message.append(message_string[digit_sum])

    # Remove the used character from the string
    message_string = message_string[:digit_sum] + message_string[digit_sum+1:]

final_message = ''.join(message)

print(final_message)
