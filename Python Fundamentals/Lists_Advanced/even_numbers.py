numbers = list(map(int, input().split(", ")))
indexing = list(map(lambda number: number if numbers[number] % 2 == 0 else "no", range(len(numbers))))
even_indexes = list(filter(lambda current_index: current_index != "no", indexing))

print(even_indexes)
