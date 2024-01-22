key = int(input())
number_of_lines = int(input())
sum_letters = ""
decrypted_message = ""
for decrypting in range(number_of_lines):
    current_letter = input()
    sum_letters = ord(current_letter) + key
    decrypted_message += chr(sum_letters)
print(decrypted_message)
