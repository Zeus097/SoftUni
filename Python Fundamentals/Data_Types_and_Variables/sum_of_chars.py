number_of_lines = int(input())
letter_sum = 0

for char in range(number_of_lines):
    current_letter = input()
    letter_sum += ord(current_letter)

print(f"The sum equals: {letter_sum}")
