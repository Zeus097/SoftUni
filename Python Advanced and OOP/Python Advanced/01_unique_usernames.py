number_of_names = int(input())
unique_collection = set()

for _ in range(number_of_names):
    current_name = input()
    unique_collection.add(current_name)

print(*unique_collection, sep='\n')
