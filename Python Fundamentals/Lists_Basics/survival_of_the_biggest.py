list_of_numbers_as_string = input().split()
numbers_count_to_remove = int(input())

list_of_numbers_as_int = []
filtrated_list = []

for current_number in list_of_numbers_as_string:
    list_of_numbers_as_int.append(int(current_number))

while numbers_count_to_remove != 0:
    min_number = min(list_of_numbers_as_int)
    list_of_numbers_as_int.remove(min_number)
    numbers_count_to_remove -= 1

for index in list_of_numbers_as_int:
    filtrated_list.append(str(index))

print(", ".join(filtrated_list))
