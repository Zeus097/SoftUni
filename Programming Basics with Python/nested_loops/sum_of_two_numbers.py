number_1 = int(input())
number_2 = int(input())
magic_number = int(input())
counter_combination = 0
we_have_combination = False
text_information = ""

for num_1 in range(number_1, number_2 + 1):
    for num_2 in range(number_1, number_2 + 1):
        counter_combination += 1

        if num_1 + num_2 == magic_number:
            we_have_combination = True
            text_information = f"Combination N:{counter_combination} ({num_1} + {num_2} = {magic_number})"

    if we_have_combination:
        break

if we_have_combination:
    print(text_information)
else:
    print(f"{counter_combination} combinations - neither equals {magic_number}")