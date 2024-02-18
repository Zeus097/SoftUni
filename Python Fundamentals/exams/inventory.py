journal_with_items = input().split(", ")
command = input()

while True:
    if command == "Craft!":
        break

    action = command.split(" - ")
    if action[0] == "Collect":
        current_item = action[1]
        if current_item not in journal_with_items:
            journal_with_items.append(current_item)
    elif action[0] == "Drop":
        current_item = action[1]
        if current_item in journal_with_items:
            journal_with_items.remove(current_item)
    elif action[0] == "Combine Items":
        action = action[1].split(":")
        old_item, new_item = action[0], action[1]
        if old_item in journal_with_items:
            old_item_index = journal_with_items.index(old_item)
            journal_with_items.insert(old_item_index + 1, new_item)
    elif action[0] == "Renew":
        current_item = action[1]
        if current_item in journal_with_items:
            journal_with_items.remove(current_item)
            journal_with_items.append(current_item)
    command = input()

print(", ".join(journal_with_items))
