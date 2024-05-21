from collections import deque


materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))
crafted_toys = {}

mapper = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while materials and magic_level:
    current_material = materials[-1]
    magic_value = magic_level[0]

    if materials[-1] == 0 and magic_level[0] == 0:
        materials.pop()
        magic_level.popleft()
        continue

    elif materials[-1] == 0:
        materials.pop()
        continue

    elif magic_level[0] == 0:
        magic_level.popleft()
        continue

    product = materials[-1] * magic_level[0]
    if product in mapper:
        crafted_toy = mapper[product]
        if crafted_toy not in crafted_toys:
            crafted_toys[crafted_toy] = 0
        crafted_toys[crafted_toy] += 1
        materials.pop()
        magic_level.popleft()

    elif product < 0:
        product = materials[-1] + magic_level[0]
        materials.pop()
        magic_level.popleft()
        materials.append(product)

    elif product > 0:
        magic_level.popleft()
        materials[-1] += 15


if (("Doll" in crafted_toys and "Wooden train" in crafted_toys) or
        ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys)):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    reversed_materials = list(reversed(materials))
    print(f"Materials left: {', '.join(map(str, reversed_materials))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for toy_name, amount in sorted(crafted_toys.items()):
    print(f"{toy_name}: {amount}")
