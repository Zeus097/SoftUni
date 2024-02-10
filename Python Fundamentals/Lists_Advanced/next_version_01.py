old_version = input().split()
new_version = []
for current_version in old_version:
    outer_version = int(current_version[0])
    midd_version = int(current_version[2])
    inner_version = int(current_version[4])
    inner_version += 1
    if inner_version > 9:
        inner_version = 0
        midd_version += 1
    if midd_version > 9:
        midd_version = 0
        outer_version += 1
    if outer_version == 9:
        break
    print(f"{outer_version}.{midd_version}.{inner_version}")
