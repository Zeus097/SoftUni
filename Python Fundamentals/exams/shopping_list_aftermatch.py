def needed_products(products):
    while True:
        command = input()
        if command == 'Go Shopping!':
            break

        action = command.split()
        if action[0] == 'Urgent':
            current_item = action[1]
            if current_item not in products:
                products.insert(0, current_item)
            else:
                continue

        elif action[0] == 'Unnecessary':
            current_item = action[1]
            if current_item in products:
                products.remove(current_item)
            else:
                continue

        elif action[0] == 'Correct':
            old_item = action[1]
            new_item = action[2]
            if old_item in products:
                old_item_index = products.index(old_item)
                products[old_item_index] = new_item
            else:
                continue

        elif action[0] == 'Rearrange':
            current_item = action[1]
            if current_item in products:
                item_index = products.index(current_item)
                item_name = products.pop(item_index)
                products.append(item_name)
            else:
                continue

    return ', '.join(products)


shopping_list = input().split('!')
groceries_list = needed_products(shopping_list)
print(groceries_list)
