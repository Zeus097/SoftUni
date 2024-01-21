number = int(input())
for first_letter in range(number):
    first_letter += 97
    for second_letter in range(number):
        second_letter += 97
        for third_letter in range(number):
            third_letter += 97
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}")

# second solution
#
# number_of_symbols = int(input())
# for first_symbol in range(number_of_symbols):
#     for second_symbol in range(number_of_symbols):
#         for third_symbol in range(number_of_symbols):
#             print(f"{chr(97+first_symbol)}{chr(97+second_symbol)}{chr(97+third_symbol)}")
