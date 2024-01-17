beginning_interval = input()
final_interval = input()
exceptional_letters = input()
counter = 0

for first_combination in range(ord(beginning_interval), ord(final_interval) + 1):
    for second_combination in range(ord(beginning_interval), ord(final_interval) + 1):
        for third_combination in range(ord(beginning_interval), ord(final_interval) + 1):
            combination = chr(first_combination) + chr(second_combination) + chr(third_combination)
            counter += 1
            if exceptional_letters in combination:
                counter -= 1
                continue
            print(combination, end=" ")
print(counter)