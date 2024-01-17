decoration_quantity = int(input())
days_left = int(input())
total_cost = 0
total_spirit = 0

ornament_set_cost = 2
tree_skirt_cost = 5
tree_garland_cost = 3
tree_lights_cost = 15

for days in range(1, days_left + 1):
    if days % 11 == 0:
        decoration_quantity += 2
    if days % 2 == 0:
        total_cost += decoration_quantity * ornament_set_cost
        total_spirit += 5
    if days % 3 == 0:
        total_cost += decoration_quantity * (tree_skirt_cost + tree_garland_cost)
        total_spirit += 3 + 10
    if days % 5 == 0:
        total_cost += decoration_quantity * tree_lights_cost
        total_spirit += 17
        if days % 3 == 0:
            total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_cost + tree_garland_cost + tree_lights_cost
if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
