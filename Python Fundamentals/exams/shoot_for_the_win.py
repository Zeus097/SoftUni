target_values = list(map(int, input().split()))
command = input()
shot_targets_counter = 0

while command != "End":
    user_index = int(command)

    if user_index >= len(target_values):
        command = input()
        continue

    for list_index in range(len(target_values)):
        if target_values[list_index] == -1:
            continue

        elif target_values[user_index] < target_values[list_index]:
            target_values[list_index] -= target_values[user_index]
        else:
            if list_index == user_index:
                continue
            target_values[list_index] += target_values[user_index]
    target_values[user_index] = -1
    shot_targets_counter += 1
    command = input()

final_score = [str(current_target) for current_target in target_values]
final_score = " ".join(final_score)
print(f"Shot targets: {shot_targets_counter} -> {final_score}")
