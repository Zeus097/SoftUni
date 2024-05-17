numbers = tuple(map(float, input().split()))
collection = {}

for current_num in numbers:
    count = numbers.count(current_num)
    if current_num not in collection:
        collection[current_num] = count

for number, count in collection.items():
    print(f"{number} - {count} times")
