number_of_names = int(input())
list_of_names = set()

for _ in range(number_of_names):
    current_name = input()
    list_of_names.add(current_name)

print(*list_of_names, sep='\n')
