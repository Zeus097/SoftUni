money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_int = []

for money in money_as_string:
    money_as_int.append(int(money))

final_sum = []
start_index = 0

for beggar in range(number_of_beggars):
    current_beggar = 0
    for current_index in range(start_index, len(money_as_int), number_of_beggars):
        current_beggar += money_as_int[current_index]
    start_index += 1
    final_sum.append(current_beggar)

print(final_sum)
