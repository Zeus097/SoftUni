string_of_numbers = input()
list_of_integers = []
zero_list = []

for number in string_of_numbers.split(", "):
    if int(number) == 0:
        zero_list.append(int(number))
    else:
        list_of_integers.append(int(number))

list_of_integers.extend(zero_list)
print(list_of_integers)
