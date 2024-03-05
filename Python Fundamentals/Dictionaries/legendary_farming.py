legendary_collection = {"Shards": 0, "Fragments": 0, "Motes": 0}
junk = {}
flag = False

while True:
    if flag:
        break

    command = input().split()
    for index in range(0, len(command), 2):

        quantity = int(command[index])
        material = command[index + 1].lower()

        if material == "Shards".lower():
            legendary_collection["Shards"] += quantity
            if legendary_collection["Shards"] >= 250:
                flag = True
                break

        elif material == "Fragments".lower():
            legendary_collection["Fragments"] += quantity
            if legendary_collection["Fragments"] >= 250:
                flag = True
                break

        elif material == "Motes".lower():
            legendary_collection["Motes"] += quantity
            if legendary_collection["Motes"] >= 250:
                flag = True
                break

        else:
            if material.lower() not in junk:
                junk[material] = 0
            junk[material] += quantity


for key, value in legendary_collection.items():
    if key == "Shards" and value >= 250:
        legendary_item = "Shadowmourne"
        print(f"{legendary_item} obtained!")
        legendary_collection[key] -= 250

    elif key == "Fragments" and value >= 250:
        legendary_item = "Valanyr"
        print(f"{legendary_item} obtained!")
        legendary_collection[key] -= 250

    elif key == "Motes" and value >= 250:
        legendary_item = "Dragonwrath"
        print(f"{legendary_item} obtained!")
        legendary_collection[key] -= 250


for key, value in legendary_collection.items():
    print(f"{key.lower()}: {value}")

for key, value in junk.items():
    print(f"{key.lower()}: {value}")
