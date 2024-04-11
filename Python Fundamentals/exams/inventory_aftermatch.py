def item_research(items):
    while True:
        command = input()
        if command == 'Craft!':
            break

        action = command.split(' - ')
        if action[0] == 'Collect':
            given_item = action[1]
            if given_item not in items:
                items.append(given_item)
            else:
                continue

        elif action[0] == 'Drop':
            item_for_deletion = action[1]
            if item_for_deletion in items:
                items.remove(item_for_deletion)
            else:
                continue

        elif action[0] == 'Combine Items':
            old_item, new_item = action[1].split(':')
            if old_item in items:
                old_item_index_position = items.index(old_item)
                items.insert(old_item_index_position + 1, new_item)
            else:
                continue

        elif action[0] == 'Renew':
            renew_item = action[1]
            if renew_item in items:
                configuration = items.pop(items.index(renew_item))
                items.append(configuration)
            else:
                continue

    return ', '.join(items)


journal_with_items = input().split(', ')
my_inventary = item_research(journal_with_items)
print(my_inventary)
