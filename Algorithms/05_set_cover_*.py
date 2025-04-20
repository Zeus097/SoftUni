def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_sets = []
    remaining_sets = sets.copy()

    while universe_set and remaining_sets:
        best_set = max(remaining_sets, key=lambda bs: len(universe_set.intersection(bs)))
        if not universe_set.intersection(best_set):
            break
        chosen_sets.append(best_set)
        universe_set -= set(best_set)
        remaining_sets.remove(best_set)

    if universe_set:
        return None
    return chosen_sets


universe_input = list(map(int, input().split(', ')))
n = int(input())
sets_collection = []

for _ in range(n):
    set_elements = list(map(int, input().split(', ')))
    sets_collection.append(set_elements)

result = set_cover(universe_input, sets_collection)

if result is None:
    print('No solution exists')
else:
    for i in range(len(result)):
        result[i] = sorted(result[i])

    print(f"\nSets to take ({len(result)}): ")
    for s in result:
        print("{", ", ".join(map(str, s)), "}")
