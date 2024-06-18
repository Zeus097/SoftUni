def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_sets = []
    remaining_sets = sets.copy()

    while universe_set and remaining_sets:
        best_set = max(remaining_sets, key=lambda s: len(universe_set.intersection(s)))
        if not universe_set.intersection(best_set):
            break
        chosen_sets.append(best_set)
        universe_set -= set(best_set)
        remaining_sets.remove(best_set)

    if universe_set:
        return None
    return chosen_sets


universe_ = list(map(int, input().split(', ')))
n = int(input())
sets_ = []

for _ in range(n):
    set_elements = list(map(int, input().split(', ')))
    sets_.append(set_elements)

result = set_cover(universe_, sets_)

if result is None:
    print("No solution exists")
else:
    for i in range(len(result)):
        result[i] = sorted(result[i])

    print(f"Sets to take ({len(result)}): ")
    for j in result:
        print("{", ", ".join(map(str, j)), "}")
