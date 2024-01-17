a = int(input())
b = int(input())
max_count = int(input())

counter = 0
first_symbol = 34
second_symbol = 63
for i in range(1, a + 1):
    for j in range(1, b + 1):
        counter += 1
        first_symbol += 1
        if first_symbol > 55:
            first_symbol = 35
        second_symbol += 1
        if second_symbol > 96:
            second_symbol = 64
        third_symbol = i
        fourth_symbol = j

        print(f'{chr(first_symbol)}{chr(second_symbol)}{third_symbol}{fourth_symbol}{chr(second_symbol)}'
              f'{chr(first_symbol)}', end='|')
        if counter == max_count:
            break
    if counter == max_count:
        break