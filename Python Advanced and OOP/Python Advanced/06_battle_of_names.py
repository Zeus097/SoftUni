num_of_names = int(input())

even_nums_set = set()
odd_nums_set = set()

for index in range(1, num_of_names + 1):
    name_value = sum([ord(char) for char in input()]) // index
    if name_value % 2 == 0:
        even_nums_set.add(name_value)
    else:
        odd_nums_set.add(name_value)

if sum(odd_nums_set) == sum(even_nums_set):
    print(*(odd_nums_set.union(even_nums_set)), sep=', ')

elif sum(odd_nums_set) > sum(even_nums_set):
    print(*odd_nums_set.difference(even_nums_set), sep=', ')
else:
    print(*odd_nums_set.symmetric_difference(even_nums_set), sep=', ')
